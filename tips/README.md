# Tips and Tricks

This section holds tips and tricks I discovered that may be of use again in the future.

## Gnome Desktop Environment under WSL

WSL (Windows Subsystem for Linux) does not feature a full Gnome Desktop, but some Gnome settings still apply when running graphical applications like Linux.

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

## Markdown

### Supported Languages for Markdown Codeblocks

A [list of supported languages](https://gist.github.com/jon3laze/2b237438ddf859a3767cab997ff0d518) for Markdown Codeblocks on Github.
