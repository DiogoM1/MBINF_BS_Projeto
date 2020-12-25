# Docker - mbinf_um/bs2020_cplex_me_toolset
versão: 1.1
data: 2020-12-23

Este *docker* fornece um métood para usar o solver CPLEX e as outras ferramentas de Engenharia Metabólica

Solvers:
- [CPLEX 1209/CPLEX 1210](https://www.ibm.com/analytics/cplex-optimizer)

Packages:
- [reframed](https://github.com/cdanielmachado/reframed)
- [cobrapy](https://github.com/opencobra/cobrapy)
- [cobamp](https://github.com/BioSystemsUM/cobamp)
- [escher](https://github.com/zakandrewking/escher)
- [mewpy](https://github.com/BioSystemsUM/mewpy)

## Criar a *docker image*

Devido à nova licença o utilizador deve criar a sua própria imagem no seu computador. Para isto deve primeiro obter uma cópia do *cplex*.

Isto pode ser feito em [IBM Académico](ibm.biz/CPLEXonAI)

O nome do ficheiro necessário para o *docker* é semelhante a "cplex_studio129.linux-x86-64.bin"

### Criar no *Windows*

Basta fazer *cd* para a diretoria do *Dockerfile* usando *PowerShell* e correr o seguinte comando nesta mesma consola

```shell script
docker build -t mbinf_um/bs2020_cplex_me_toolset:1.1 -t mbinf_um/bs2020_cplex_me_toolset:latest .
```

### Criar no *Bash/WSL2/Zsh(Mac os)*

Basta fazer *cd* para a diretoria do *Dockerfile* usando o terminal e correr o seguinte comando nesta mesma consola

```shell script
bash build_docker.sh
```

## Correr a *docker image*

### Correr no *Windows/Mac OS*

Ler [Docker Docs](https://docs.docker.com/desktop/dashboard/#run-an-image-as-a-container)

Não esquecer de especificar 2 opções:
- volume, como a diretoria do código do projeto
- porta, 8888:8888

### Correr em *Bash/WSL2/Zsh(Mac OS)*

Um exemplo do comando para correr é

```shell script
docker run --rm -v /home/dm/PycharmProjects/MBINF_BS_Projeto/:/opt/project/ -p 8888:8888 -it mbinf_um/bs2020_cplex_me_toolset:1.1
```

Basta adaptar à diretória onde tens o projeto.
A pasta interna no *docker* é "/opt/project/" porque esta é a que o PyCharm usa quando usa um *docker* como interpertador. Como tal preferi harmonizar em todos, mas pode ser outra. 

### Correr como *interperter* no *PyCharm*

Ler [Configure an interpreter using Docker﻿](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html#debug)

É melhor no passo [Preferences](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html#config-docker)

Adicionar um *Path Mapping* entre a diretoria do projeto no nosso *OS* e "/opt/project/" no *docker*

Pode também ser ùtil ler [Docker in Pycharm](https://www.jetbrains.com/help/pycharm/docker.html#run-containers) para perceber melhor este sistema

## Correr o *Jupyter*

Depois de correr a imagem, basta correr o seguinte comando.

```shell script
jupyter notebook --ip=0.0.0.0
```

Este corre o *jupyter notebook* e formata este de maneira a passar para fora do *container*. De seguida irá aparecer o link que se deve aceder no browser ou pycharm para ter acesso ao *Jupyter*