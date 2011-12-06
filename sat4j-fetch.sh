#!/bin/sh
name=sat4j
tag=2_1_1
version=2.1.1
tar_name=$name-$version

rm -fr $tar_name && mkdir $tar_name
pushd $tar_name

# Fetch plugins
svn co svn://svn.forge.objectweb.org/svnroot/sat4j/maven/tags/$tag .

popd
# create archive
tar -cjf $tar_name.tar.bz2 $tar_name
