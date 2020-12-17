[![img](https://img.shields.io/badge/Lifecycle-Experimental-339999)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# Verifiable Credential Visual Verifier

VC Visual Verifier is a utility designed to provide visual feedback when authenticating using a Verifiable Credential using [vc-authn-oidc](https://github.com/bcgov/vc-authn-oidc).

To run the development server, first run `./manage build` from the [docker](./docker) folder, then `./manage start`.

For use containers suitable for production, use `./manage start-prod` after building the images.

The content of the landing page can be customized or overridden at deployment time by editing/replacing [custom_home.html](./src/static/custom_home.html).
