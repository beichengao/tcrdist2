"""

For builds in Travis CI, some large files may need to be downloaded prior to tests.


"""
import os
import sys

def install_test_files():
    install_dropbox_file("mouse_pairseqs_v1_parsed_seqs_probs_mq20_clones.tsv",
                         "https://www.dropbox.com/s/l0z12f8lc752wfx/mouse_pairseqs_v1_parsed_seqs_probs_mq20_clones.tsv?dl=1",
                         "test_files")
    install_dropbox_file("vdjDB_PMID28636592.tsv",
                         "https://www.dropbox.com/s/f5kxikmv4s95dry/vdjDB_PMID28636592.tsv?dl=0",
                         "test_files")


def install_dropbox_file(filename,
                         download_link,
                         install_dir = "test_files"):#
    """
    Function installs from a download link using curl

    Parameters
    ----------
    download_file : string

    Returns
    -------
    curl_url_cmd : string
        the command for installing to tcrdist/db/alphabeta_db.tsv_files/*

    """
    assert isinstance(filename, str), "filename must be a string"
    assert isinstance(download_link, str), "download link must be a string"
    assert isinstance(install_dir, str), "install_dir must be a string"  # TODO: Consider in future nested directory case tcrdist/X/Y, you could use reduce os os.path.join()

    # Where the file is to be installed
    path_file = os.path.realpath(__file__)
    path = os.path.dirname(path_file)

    assert os.path.isdir(os.path.join(path, install_dir)), "The target directory for download does not exist"

    install_path = os.path.join(path, install_dir, filename)

    def generate_curl(fn, link):
        return('curl -o {} {} -L'.format(fn, link))

    curl_url_cmd = generate_curl(install_path, download_link)
    print("RUNNING: {}\n".format(curl_url_cmd) )
    os.system(curl_url_cmd)
    return(curl_url_cmd)
