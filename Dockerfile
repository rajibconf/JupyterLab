FROM jupyter/base-notebook:latest

RUN conda install --quiet --yes \
    'jupyterlab=3.2.0' \
    && conda clean --all -f -y \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

EXPOSE 8888
