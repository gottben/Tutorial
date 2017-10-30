import numpy 
import tensorflow
from gnuradio import gr

class tf_adder(gr.sync_block):
  """
  docstring for block tf_adder
  """
  x = tensorflow.placeholder("complex64")
  y = tensorflow.placeholder("complex64")
  def __init__(self):
    gr.sync_block.__init__(self,
        name="tf_adder",
        in_sig=[numpy.complex64,numpy.complex64],
        out_sig=[numpy.complex64])
    self.sess = tensorflow.Session()
    self.op = tensorflow.add( self.x, self.y)
    
  def work(self, input_items, output_items):
      in0 = self.sess.run([self.op], feed_dict={self.x:input_items[0],self.y:input_items[1]})
      output_items[0][:] = in0[0]
      # <+signal processing here+> 
      return len(in0[0]) 
      
   
