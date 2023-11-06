from omegaconf import OmegaConf

args = OmegaConf.from_cli()
cfg = OmegaConf.load(args.config)
del args['config']

cfg = OmegaConf.merge(cfg, args)

print(OmegaConf.to_yaml(cfg))
