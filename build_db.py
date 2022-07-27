import glob
import os

from absl import app
from absl import flags
from google.protobuf import text_format

from proto import person_pb2

FLAGS = flags.FLAGS
flags.DEFINE_string('data_dir', '', 'Directory containing .textproto data.')


def main(argv):
  file_names = glob.glob(os.path.join(FLAGS.data_dir, '*.textproto'))
  for file_name in file_names:
    text_proto = open(file_name, 'r').read()
    try:
      person = text_format.Parse(text_proto, person_pb2.Person())
    except text_format.ParseError as e:
      raise text_format.ParseError('Error parsing {}'.format(os.path.basename(file_name))) from e
    print(person)


if __name__ == "__main__":
  app.run(main)
