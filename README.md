# Project Poultry
![Static Badge](https://img.shields.io/badge/github-repo-blue?logo=github&link=https%3A%2F%2Fgithub.com%2FquietCoder500%2Fproject_poultry)

Project Poultry is an open source website designed to enable better record keeping for 4-H'ers, FFA youth, and hobby farmers. It employs two concepts called Milestones and Progress Reports to help you make data-backed changes to your project during the project and builds a reference if you do the project again.

> [!NOTE]
> ## Admissions reviewers!
> Very soon I will have a link to a demo of the website. To access the site click the link at the top right corner of you screen and select 'Continue as Guest.'

## Terms

> [!IMPORTANT]
> Project Poultry's structure is designed around the idea of projects. A project is exactly what it sounds like. There are two types of projects: A still project or a livestock project. A livestock project is for when you are raising livestock and each herd/flock/etc. is has a dedicated project. A still project is for everything else (Beekeeping, gardening, baking). If you are a youth member of FFA or 4-H, this will be a familiar concept to you.


Project Poultry has two main concepts: Milestones and Progress Reports. Take a second to familiarize yourself these two ideas before you start.

### Milestones

**A milestone is some important event or change that happens during the project. You can reference milestones later on a timeline so you can improve the next year of the project.** For example, if you were raising a flock of market turkeys, then you would record events like animal pickup, moving flock locations, diet changes, bedding changes, and sale dates.

(_Milestones are available for both still and livestock project types_)

### Progress Reports
**A progress report is a snapshot of the growth and current status of your livestock. You can use the report to make changes to your project as the project goes on.** You can report several types of data to Project Poultry including individual animal weights and herd feed consumption. These different metrics are then used to generate charts, graphs, and rates that will help you understand how well your project is going. For example, if you were raising market poultry, then you could log each chicken's weight and log each time you had to open a new bag of feed. 

(_Progress Reports are currently only available for livestock projects types_)

## Quickstart

### Development testing
This is for advanced users only. **You will not need to do this.**

1. Install Python, the UV package manager, and Just on your machine.
2. Clone this project from Github and enter the directory
3. Run `uv venv` and read the output to find the command to enter the new virtual environment.
4. Run `uv sync` to install the needed packages
5. Now you can start the server by running `just` in one terminal and `just css` in a second terminal. This will start the server and automatically recompile the css and js on change.
