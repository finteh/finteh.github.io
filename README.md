# finteh.github.io
[![github pages](https://github.com/finteh/finteh.github.io/workflows/github%20pages/badge.svg)](https://github.com/finteh/finteh.github.io/actions?query=workflow%3A%22github+pages%22)

This is the repository of [finteh.org](https://finteh.org/).

You are now on the default ```source``` branch, which is a [Hugo](https://gohugo.io/) project. Website itself is hosted by [Github Pages](https://pages.github.com/) from the root of the ```master``` branch, which has an independent history of commits deployed automatically by [github pages workflow](.github/workflows/gh-pages.yml) with each push in the ```source``` branch.


## Installation and launch
1. [Install Hugo](https://gohugo.io/getting-started/installing/).

   If you're on Debian or Ubuntu the recommended option is installing snap package:

   ```bash
   snap install hugo
   ```

   If you don't have snap pre-installed, install it:

   ```bash
   sudo apt update
   sudo apt install snapd
   ```

2. Clone the repository:

   ```bash
   git clone --recurse-submodules git@github.com:finteh/finteh.github.io.git
   ```

   If you don't have SSH keys associated with your GitHub account then clone via HTTPS:

   ```bash
   git clone --recurse-submodules https://github.com/finteh/finteh.github.io.git
   ```

3. Launch webserver:

   ```bash
   cd finteh.github.io
   hugo server
   ```

4. Open site in your browser (default address is http://localhost:1313/).


## Contributing
Work from the ```source``` branch, don't use the ```master``` branch for contributions, only for hosting.

You can change data used to build site in configuration files in the [data/](data) folder and static content in the [static/](static) folder. You can also change theme in the [themes/somrat/](themes/somrat) folder, which is a [separate repository](https://github.com/fincubator/somrat).

Refer to [Hugo documentation](https://gohugo.io/getting-started/directory-structure/) for more information.
