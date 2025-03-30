# Highglade

## Dependencies:

```sh
brew install $(<brew.txt)
```

## Talhelper setup


## History
Added annotations for openebs
 
```
kubectl label ns openebs \
  pod-security.kubernetes.io/audit=privileged \
  pod-security.kubernetes.io/enforce=privileged \
  pod-security.kubernetes.io/warn=privileged
```
