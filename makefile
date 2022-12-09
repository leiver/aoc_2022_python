help: 
	@echo "Commands:"
	@echo " - help: 	show this help"
	@echo " - new:		create a new file for today"
	@echo " - readme: 	build the new readme with links"

setup: 
	@touch session.cookie
	@mkdir -p inputs
	@make help

new: 
	@python aoc_2022_python/utils/new_file.py