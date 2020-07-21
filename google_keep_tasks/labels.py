import click

from google_keep_tasks.utils import pretty_date


def format_label(label):
    return u'━ {}'.format(label)


def format_label_with_timestaps(label):
    return u'{} (created {}, updated {})'.format(
        format_label(label),
        pretty_date(label.timestamps.created),
        pretty_date(label.timestamps.updated),
    )


@click.group()
def labels():
    """Gkeep can manage Google Keep labels using ``labels`` command.
    This command has subcommands for adding, searching, editing, or
    deleting labels. To see all subcommands of ``labels`` use ``--help``::

        gkeep labels --help

    An example of a subcommand is ``add``. To see help use
    ``gkeep labels add --help``.
    """
    pass


@labels.command('list')
@click.option('--timestamps', is_flag=True, help='Include timestaps per each label.')
@click.pass_context
def list_labels(ctx, timestamps):
    """List labels on Google Keep. For example:

    .. code-block:: shell

        gkeep labels list

    The syntax is:
    """
    keep = ctx.obj['keep']
    fmt = format_label_with_timestaps if timestamps else format_label
    click.echo(u'\n'.join([
         fmt(label) for label in keep.labels()]
    ))
