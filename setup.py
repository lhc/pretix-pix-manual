from setuptools import setup


setup(
    entry_points="""
[pretix.plugin]
pretix_pix_manual=pretix_pix_manual:PretixPluginMeta
"""
)
