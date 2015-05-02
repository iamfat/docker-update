# -*- coding: utf-8 -*-

import subprocess
import sys
import getopt

def usage():
    print "Usage: docker-update [container]|[-a]\n"

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "a")
    except getopt.GetoptError as e:
        # print help information and exit:
        usage()
        sys.exit(2)

    enum_all = False
    for o, a in opts:
        if o == "-a":
            enum_all = True

    # enumerate all containers using these images
    if len(args) > 0:
        containers = args
    else:
        # enumerate all containers via `docker ps`
        try:
            containers = subprocess.check_output("docker ps -q" if enum_all else "docker ps -aq", shell=True).splitlines()
        except subprocess.CalledProcessError as e:
            print ("%s" % str(e))
            sys.exit()

        def readable_name(container):
            try:
                return subprocess.check_output(
                            "docker inspect -f {{.Name}} %s" % container, 
                            shell=True).lstrip('/').rstrip('\n')
            except subprocess.CalledProcessError as e:
                return container
        containers = map(readable_name, containers)            
    
    run_commands = []
    images = set()
    for container in containers:
        try:
            images.add(
                subprocess.check_output(
                    "docker inspect -f {{.Config.Image}} %s" % container, 
                    shell=True).rstrip('\n'))
                    
            run_commands.append("\n# Update %s" % container)
            run_commands.append("docker rm -f %s" % container)
            run_commands.append(
                subprocess.check_output(
                    "docker-parse %s" % container, shell=True).rstrip('\n'))
        except subprocess.CalledProcessError as e:
            continue

    pull_commands = [ "# Update images"]
    for image in images:
        pull_commands.append("docker pull %s" % image)

    print('\n'.join(pull_commands))
    print('\n'.join(run_commands))

if __name__ == "__main__":
    main()