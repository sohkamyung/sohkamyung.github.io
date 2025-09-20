# Tips and Tricks

[Main Index](../README.md)

This section holds tips and tricks I discovered that may be of use again in the future.

## Gnome Desktop Environment under WSL

WSL (Windows Subsystem for Linux) does not feature a full Gnome Desktop, but some Gnome settings still apply when running graphical applications like Emacs.

Gnome settings can be change by using `gsettings` or `dconf-editor`. Examples below will use `gsettings`.

### Adjusting Cursor Size in WSL

To see the current cursor size:

```shell
> gsettings get org.gnome.desktop.interface cursor-size
24
```

To set the current cursor size:

```shell
> gsettings set org.gnome.desktop.interface cursor-size <value>
```

*Added: 2025/08/16.*

### Adjusting GUI Window Button Layout

To see the current button layout:

```shell
> gsettings get org.gnome.desktop.wm.preferences button-layout
'appmenu:close'
```

To set the current button layout to show the appmenu on the left and  the standard minimise, maximise and close buttons on the right:

```shell
> gsettings set org.gnome.desktop.wm.preferences button-layout "appmenu:minimize,maximize,close"
```

*Added: 2025/08/16.*

## Markdown

### Supported Languages for Markdown Codeblocks

A [list of supported languages](https://gist.github.com/jon3laze/2b237438ddf859a3767cab997ff0d518) for Markdown Codeblocks on Github.

*Added: 2025/08/16.*

## Using `yt-dlp`

[`yt-dlp`](https://github.com/yt-dlp/yt-dlp) is a command-line tool to download Video/Audio from various sites. The `ffmpeg` library may be required.

Options I use to:

- download playlist in the best audio in Opus (preferred) or Ogg Vorbis (deprecated) formats, output filename based on playlist index, title and extension and restricted to Windows filenames

```shell
yt-dlp -f bestaudio --extract-audio --audio-format <opus/vorbis> -o "%(playlist_index)s-%(track)s.%(ext)s" --windows-filenames <link>
```

*Added: 2025/08/24.*

## Git Related Tips

### Git Cheat Sheet

A [Git Cheat Sheet](https://git-scm.com/cheat-sheet), summarizing ways to execute `git` for various tasks.

*Added: 2025/09/20.*

### Partial and Shallow Git Clones

You don't have to pull every revision from a git repository when cloning it. It is possible to work with a local git repository that is a minimal clone of the main git repository.

- `git clone --filter=blob:none <url>` creates a *blobless clone* for doing development on the latest version of code on a git repository
- `git clone --filter=tree:0 <url>` creates a *treeless clone* for doing a single build from a git repository, but where you still need to access its history
- `git clone --depth=1 <url>` creates a *shallow clone* for doing a single build that will be thrown away

This [Github blog post](https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/) gives an explanation of the three options.

*Added: 2025/09/07.*

## Zoom

### Fixing Audio Output Issues

Some laptops have Realtek Audio Drivers with noise cancellation. For unknown reasons, the audio driver believes audio from Zoom is noise and cancels it, muting Zoom output. Disabling noise cancellation in the driver fixes the issue.

Fix discovered in this response in a [Zoom Community Post](https://community.zoom.com/t5/Zoom-Meetings/Audio-not-working-on-Zoom-desktop-with-brand-new-laptop-all/m-p/174217/highlight/true#M98271).

*Added: 2025/09/07.*

## Computer Related History

### Story of Creative Technology

The story of the Singapore company the created the Sound Blaster, [Creative Technology](https://www.abortretry.fail/p/the-story-of-creative-technology), from its beginning to the present day. [Internet Archive Link](https://web.archive.org/web/20250911040355/https://www.abortretry.fail/p/the-story-of-creative-technology)

*Added: 2025/09/20.*

## Nature Related Links

### iNaturalist Resources

A link to a list of [iNaturalist Resources](https://www.inaturalist.org/pages/resources) to reference for introducing [iNaturalist](https://www.inaturalist.org/) to other people, and how to use iNaturalist to make observations and identification of wild organisms.

*Added: 2025/09/20.*
