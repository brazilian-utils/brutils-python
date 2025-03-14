from typing import List, Literal, Optional, TypedDict

from brutils.data.enums import UF, CODE_TO_UF


class Porte(TypedDict):
    """
    Company size classification information.
    
    Args:
        id: Size classification code.
        descricao: Size classification description (e.g., "Micro Empresa").
    """
    id: str
    descricao: str

class NaturezaJuridica(TypedDict):
    """
    Legal nature of the company.
    
    Args:
        id: Legal nature code.
        descricao: Legal nature description (e.g., "Sociedade Empresária Limitada").
    """
    id: str
    descricao: str

class QualificacaoResponsavel(TypedDict):
    """
    Qualification of the company's responsible person.
    
    Args:
        id: Qualification code.
        descricao: Qualification description (e.g., "Sócio-Administrador").
    """
    id: int
    descricao: str

class Pais(TypedDict):
    """
    Country information.
    
    Args:
        id: Country ID.
        iso2: ISO 3166-1 alpha-2 code.
        iso3: ISO 3166-1 alpha-3 code.
        nome: Country name.
        comex_id: Foreign trade ID.
    """
    id: str
    iso2: str
    iso3: str
    nome: str
    comex_id: str

class QualificacaoSocio(TypedDict):
    """
    Partner qualification information.
    
    Args:
        id: Qualification code.
        descricao: Qualification description.
    """
    id: int
    descricao: str

class Socio(TypedDict):
    """
    Company partner/shareholder information.
    
    Args:
        cpf_cnpj_socio: Partially masked partner's CPF (individual) or CNPJ (company).
        nome: Partner's name.
        tipo: Partner type (e.g., "Pessoa Física").
        data_entrada: Date when partner joined the company.
        cpf_representante_legal: CPF of legal representative (if any).
        nome_representante: Name of legal representative.
        faixa_etaria: Age range of the partner.
        atualizado_em: Last update timestamp.
        pais_id: Country ID of the partner.
        qualificacao_socio: Partner's qualification in the company.
        qualificacao_representante: Representative's qualification (if applicable).
        pais: Country information.
    """
    cpf_cnpj_socio: str
    nome: str
    tipo: str
    data_entrada: str
    cpf_representante_legal: str
    nome_representante: Optional[str]
    faixa_etaria: str
    atualizado_em: str
    pais_id: str
    qualificacao_socio: QualificacaoSocio
    qualificacao_representante: Optional[str]
    pais: Pais

class Simples(TypedDict):
    """
    Information about the company's participation in Simples Nacional tax regime.
    
    Args:
        simples: Whether the company is in Simples Nacional.
        data_opcao_simples: Date the company opted into Simples Nacional.
        data_exclusao_simples: Date the company left Simples Nacional (if applicable).
        mei: Whether the company is registered as MEI (Individual Microentrepreneur).
        data_opcao_mei: Date the company registered as MEI.
        data_exclusao_mei: Date the company left MEI status.
        atualizado_em: Last update timestamp.
    """
    simples: Literal["Sim", "Não"]
    data_opcao_simples: Optional[str]
    data_exclusao_simples: Optional[str]
    mei: Literal["Sim", "Não"]
    data_opcao_mei: Optional[str]
    data_exclusao_mei: Optional[str]
    atualizado_em: str

class AtividadeEconomica(TypedDict):
    """
    Economic activity classification.
    
    Args:
        id: CNAE (National Classification of Economic Activities) code.
        secao: CNAE section.
        divisao: CNAE division.
        grupo: CNAE group.
        classe: CNAE class.
        subclasse: CNAE subclass.
        descricao: Activity description.
    """
    id: str
    secao: str
    divisao: str
    grupo: str
    classe: str
    subclasse: str
    descricao: str

class Estado(TypedDict):
    """
    Brazilian state information.
    
    Args:
        id: State ID.
        nome: State name.
        sigla: State abbreviation.
        ibge_id: IBGE (Brazilian Institute of Geography and Statistics) code.
    """
    id: int
    nome: Literal[tuple(UF.values)]
    sigla: Literal[tuple(UF.names)]
    ibge_id: Literal[tuple(CODE_TO_UF.values)]

class Cidade(TypedDict):
    """
    City information.
    
    Args:
        id: City ID.
        nome: City name.
        ibge_id: IBGE code.
        siafi_id: SIAFI (Integrated System of Financial Administration) code.
    """
    id: int
    nome: str
    ibge_id: int
    siafi_id: str

class Estabelecimento(TypedDict):
    """
    Establishment information (physical location of the company).
    
    Args:
        cnpj: Full CNPJ number.
        atividades_secundarias: List of secondary economic activities.
        cnpj_raiz: Base CNPJ (first 8 digits).
        cnpj_ordem: CNPJ order number (4 digits).
        cnpj_digito_verificador: CNPJ check digits (2 digits).
        tipo: Establishment type (e.g., "Matriz").
        nome_fantasia: Trade name.
        situacao_cadastral: Registration status.
        data_situacao_cadastral: Date of current registration status.
        data_inicio_atividade: Activity start date.
        nome_cidade_exterior: Foreign city name (if applicable).
        tipo_logradouro: Street type.
        logradouro: Street name.
        numero: Address number.
        complemento: Address complement.
        bairro: Neighborhood.
        cep: ZIP code.
        ddd1: Area code for primary phone.
        telefone1: Primary phone number.
        ddd2: Area code for secondary phone.
        telefone2: Secondary phone number.
        ddd_fax: Area code for fax.
        fax: Fax number.
        email: Contact email.
        situacao_especial: Special status (if any).
        data_situacao_especial: Date of special status.
        atualizado_em: Last update timestamp.
        atividade_principal: Main economic activity.
        pais: Country information.
        estado: State information.
        cidade: City information.
        motivo_situacao_cadastral: Reason for current registration status.
        inscricoes_estaduais: State registration numbers.
    """
    cnpj: str
    atividades_secundarias: List[AtividadeEconomica]
    cnpj_raiz: str
    cnpj_ordem: str
    cnpj_digito_verificador: str
    tipo: str
    nome_fantasia: str
    situacao_cadastral: str
    data_situacao_cadastral: str
    data_inicio_atividade: str
    nome_cidade_exterior: Optional[str]
    tipo_logradouro: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cep: str
    ddd1: str
    telefone1: str
    ddd2: str
    telefone2: str
    ddd_fax: Optional[str]
    fax: Optional[str]
    email: str
    situacao_especial: Optional[str]
    data_situacao_especial: Optional[str]
    atualizado_em: str
    atividade_principal: AtividadeEconomica
    pais: Pais
    estado: Estado
    cidade: Cidade
    motivo_situacao_cadastral: Optional[str]
    inscricoes_estaduais: List[str]

class CnpjData(TypedDict):
    """
    Complete data for a company registered in the Brazilian Federal Revenue system.
    
    Args:
        cnpj_raiz: Base CNPJ (first 8 digits).
        razao_social: Company's official registered name.
        capital_social: Company's capital (in BRL).
        responsavel_federativo: Federal responsible entity.
        atualizado_em: Last update timestamp.
        porte: Company size information.
        natureza_juridica: Legal nature information.
        qualificacao_do_responsavel: Responsible person qualification.
        socios: List of partners/shareholders.
        simples: Simples Nacional tax regime information.
        estabelecimento: Physical establishment information.
    """
    cnpj_raiz: str
    razao_social: str
    capital_social: str
    responsavel_federativo: str
    atualizado_em: str
    porte: Porte
    natureza_juridica: NaturezaJuridica
    qualificacao_do_responsavel: QualificacaoResponsavel
    socios: List[Socio]
    simples: Simples
    estabelecimento: Estabelecimento
