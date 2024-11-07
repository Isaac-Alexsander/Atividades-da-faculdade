class No:
    def __init__(self, val):
        self.val = val
        self.esq = None
        self.dir = None

    def mostra_no(self):
        print(self.val)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, val):
        novo = No(val)
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if val < atual.val:
                    atual = atual.esq
                    if atual is None:
                        pai.esq = novo
                        return
                else:
                    atual = atual.dir
                    if atual is None:
                        pai.dir = novo
                        return

    def pesquisar(self, val):
        atual = self.raiz
        while atual is not None and atual.val != val:
            if val < atual.val:
                atual = atual.esq
            else:
                atual = atual.dir
        return atual

    def pre_ordem(self, no):
        if no is not None:
            print(no.val)
            self.pre_ordem(no.esq)
            self.pre_ordem(no.dir)

    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esq)
            print(no.val)
            self.em_ordem(no.dir)

    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esq)
            self.pos_ordem(no.dir)
            print(no.val)

    def excluir(self, val):
        if self.raiz is None:
            print('A árvore está vazia')
            return False

        atual = self.raiz
        pai = self.raiz
        e_esq = True

        while atual is not None and atual.val != val:
            pai = atual
            if val < atual.val:
                e_esq = True
                atual = atual.esq
            else:
                e_esq = False
                atual = atual.dir

        if atual is None:
            return False

        if atual.esq is None and atual.dir is None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esq:
                pai.esq = None
            else:
                pai.dir = None

        elif atual.dir is None:
            if atual == self.raiz:
                self.raiz = atual.esq
            elif e_esq:
                pai.esq = atual.esq
            else:
                pai.dir = atual.esq

        elif atual.esq is None:
            if atual == self.raiz:
                self.raiz = atual.dir
            elif e_esq:
                pai.esq = atual.dir
            else:
                pai.dir = atual.dir

        else:
            sucessor = self.get_sucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esq:
                pai.esq = sucessor
            else:
                pai.dir = sucessor
            sucessor.esq = atual.esq

        return True

    def get_sucessor(self, no):
        pai_suc = no
        suc = no
        atual = no.dir
        while atual is not None:
            pai_suc = suc
            suc = atual
            atual = atual.esq

        if suc != no.dir:
            pai_suc.esq = suc.dir
            suc.dir = no.dir

        return suc
