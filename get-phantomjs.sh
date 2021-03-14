#!/bin/sh

# Download and install phantomjs; the version on Debian doesn't work with the
# grading scripts, since it's missing phantom.clearCookies(), has some kind of
# broken require(), and other fun things.

# NOTE: this probably needs to be updated for future use.
PHANTOMJS=phantomjs-2.1.1-linux-i686
if [ ! -e "$HOME/phantomjs" ]; then
  echo "One moment, downloading PhantomJS..."
  TEMPFILE=$(mktemp)
  TEMPDIR=$(mktemp -d)
  wget "https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOMJS.tar.bz2" -O "$TEMPFILE"
  echo "Unpacking..."
  tar -C "$TEMPDIR" -xjf "$TEMPFILE"
  mv "$TEMPDIR/$PHANTOMJS/bin/phantomjs" "$HOME"
  # Cleanup
  rm "$TEMPFILE"
  rm -rf "$TEMPDIR"
  echo "Done"
fi
