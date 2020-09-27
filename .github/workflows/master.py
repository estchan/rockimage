name: Publish image
on:
  branch:
    master

jobs:
  test_and_publish:
    name: publish
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repo
        uses: actions/checkout@v2
      - name: Push to GitHub Packages
        uses: docker/build-push-action@v1
        with:
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
          registry: docker.pkg.github.com
          repository: mnbbrown/rockimage/rockimage
          tag_with_ref: true
