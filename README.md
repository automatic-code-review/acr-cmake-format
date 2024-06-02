# acr-extension-name

Extensão para verificar formatação de arquivo do cmake (CMakeLists.txt e .cmake) usando a ferramenta cmake-format

1. Propriedade config se refere ao caminho para o arquivo de configurações usado pelo cmake-format, caso não possua este, uma versão com configurações padrão pode ser obtida pelo comando abaixo
```
cmake-format --dump-config [{yaml,json,python}]
```

Arquivo config.json

```json
{
  "config": ""
}
```

Dependencias

cmake-format
```
sudo apt-get install cmake-format
```