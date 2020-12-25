# Docker - mbinf_um/bs2020_cplex_me_toolset
versão: 1.1
data: 2020-12-23

Este *docker* fornece um métood para usar o solver CPLEX e as outras ferramentas de Engenharia Metabólica

## Criar o docker

### Criar no Windows

### Criar no Bash/WSL2

```shell script
bash build_docker.sh
```

## Correr o docker

### Correr no Windows

### Correr em Bash/WSL2

```shell script
docker run --rm -v /home/dm/PycharmProjects/MBINF_BS_Projeto/:/opt/project/ -p 8888:8888 -it mbinf_um/bs2020_cplex_me_toolset:1.1
```

### Correr como *interperter* no *PyCharm*

## Correr o Jupyter

```shell script
jupyter notebook --ip=0.0.0.0
```