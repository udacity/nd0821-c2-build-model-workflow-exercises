# Instructions
In this exercise you will write a script that uploads an artifact to Weights & Biases.

## Steps

1. Modify the script ``upload_artifact.py``. This script receives the following parameters:
   * ``input_file``: the path to an input file that will be uploaded as artifact
   * ``artifact_name``: the name to be used for the artifact
   * ``artifact_type``: the type of the artifact
   * ``artifact_desc``: a description for the artifact
   Inside the script you will find instructions about what to do.

2. Run the script using as ``input_file`` the path to the provided 
``zen.txt`` file, and fill the other parameters reasonably. For example:
   ```bash
   python upload_artifact.py --input_file zen.txt \
                 --artifact_name zen_of_python \
                 --artifact_type text_file \
                 --artifact_description "20 aphorisms about writing good python code"
   ```
   This artifact will contain the Zen of Python 
   (19 aphorisms about designing Python code), that you can also find by simply writing
   ``import this`` in a python script or terminal.

3. Go to W&B and check that the artifact exists at version ``v0``
4. Open the file ``zen.txt`` and change something (anything works)
5. Re-run the script, then go to W&B and check that now the artifact has a version ``v1`` containing
   the modified version. Notice now how the ``latest`` tag has moved to ``v1``.
6. Re-run again the script without changing the file, and then check that W&B recognizes that the
   artifact did not change and it does NOT create a ``v2``
7. Modify the script ``use_artifact.py``. Instructions are contained within the file.
8. Run the script:
   ```bash
   python use_artifact.py --artifact_name exercise_1/zen_of_python:v1
   ```
   You will see the content of the artifact printed on the screen. Play with the versions and
   check that v0 and v1 differ.
   
9. Go to W&B, in the Artifacts section, select the artifact ``exercise_1/zen_of_python`` and look
   at the Graph view. You will see your first very simple pipeline.