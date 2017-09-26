#!/usr/bin/python3

from polarity import type_file_enum
from polarity import process_list as SentimentAnalysis
from optparse import OptionParser


def get_comments_for(entity):
    

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="file", default="lexicons/politico.csv", help="name of the file with the lexicons")
    parser.add_option("-s", "--separator", dest="sep", default="\t", help="specify separator for the file with the lexicons")
    (options, args) = parser.parse_args()

    analyzer = SentimentAnalysis()
    analyzer.load_list(type_file_enum.polarity, options.file, options.sep)

    print(analyzer.process_text("Me gusta la nueva ley de ciencia innovación y tecnologia, Pero algo anda mal  ? "))
    print(analyzer.process_text("Así lo afirmó Jaime Velilla Castrillón, representante del Departamento en esta Junta ante las revelaciones de este diario sobre presunta corrupción. Conozca más detalles de su respuesta: A la Junta de Plaza Mayor no le hablaron con la verdad Gobernación de Antioquia"))
    print(analyzer.process_text("Jajajajaja valiente justicia alcahueta, a todos los políticos corruptos les están dando casa por cárcel, que vergüenza. Con razón tantos corruptos, saben que la justicia es laxa entonces llegan a un acuerdo se declaran culpables y les dan una mínima pena en su casa.👎👎👎👎👎"))
    print(analyzer.process_text("Más años de cárcel y menos casa por cárcel para políticos corruptos y ladrones de cuello blanco."))
    print(analyzer.process_text("Álvaro Uribe es el mejor presidente de todos los tiempos."))
    print(analyzer.process_text("Álvaro Uribe es el peor presidente de todos los tiempos."))
    print(analyzer.process_text("Álvaro Uribe es el unico presidente que se atreve a decir la verdad"))
    print(analyzer.process_text("Álvaro Uribe lo unico que sabe decir son mentiras"))