# Local Carbon Footprinter
Local Carbon Footprinter is light-weight tool designed to monitor machine usage and calculate its carbon impact. This tool is currently under **active development**, with the intention to output the raw metrics to a local flask endpoint (Phase I), integrate with the [Cloud Carbon Footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint) tool as an [On-Premise data source](https://www.cloudcarbonfootprint.org/docs/on-premise). (Phase II), and finally, to create a user-friendly desktop application (Phase III).

**Phase IV:** integrate as a module in the [GovA11y](https://github.com/GovA11y) & [Equalify](https://github.com/EqualifyApp) Ecosystems.

**Please note: This tool is currently in Phase I.**

## Getting Started
Make sure you've got docker...

**TODO** Dockerfile...
**TODO** Refactor the thing to use Flask Blueprints & not be beautiful mind layout

Deploy the Local Carbon Footprinter container using the following command:
```dockerfile
docker pull theboatymcboatface/local-carbon-footprinter:latest
```

### Docker Vars
| Variable | Description | Default | Options |
|-----------|-----------|-----------|-----------|
| LOG_LEVEL     | How many logs do you want?     | INFO | DEBUG,INFO,WARNING,ERROR,CRITICAL |
| APP_PORT | Which port should the web app use? | 3000 | Any Port Number |
| **TODO** MachineType | What type of machine is this? | server | server, laptop, desktop |
| **TODO** MachineName | Name of unique machine | Physical Host Name | Whatever you want |


### Volumes & Data
If a route is not defined or a volume is not specified, a default volume will be created. The SQLite database 'db/carbon_footprint.sqlite' storing the footprint data does not require SSDs or any specialized storage infrastructure.


## Using the Thing
**TODO** Once local dev complete


## Contributing
Interested in contributing? Fantastic! I'm not quite there yet...

**TODO**
- [ ] Github Action Automations
- [ ] Good First Tasks
- [ ] Github Project
- [ ] Protect Branches
- [ ] Dependabot
- [ ] Supply chain things...

## License
This project is open source. Contributions, suggestions, and improvements are welcome.

Open Source FTW. [GPL-3](LICENSE)
