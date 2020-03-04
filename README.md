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
You can change data used to build site in configuration files in the ```data/``` folder and static content in the ```static/``` folder. Refer to [Hugo documentation](https://gohugo.io/getting-started/directory-structure/) for more information.
