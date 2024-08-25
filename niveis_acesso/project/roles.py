from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    avaible_permissions = {'criar_metas': True, 'ver_metas':True}


class Vendedor(AbstractUserRole):
    avaible_permissions = {'acessar_produtos':True, 'ver_metas':True}
