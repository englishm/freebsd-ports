--- apps/osmocom_siggen_base.py.orig	2018-08-15 17:53:26 UTC
+++ apps/osmocom_siggen_base.py
@@ -109,9 +109,9 @@ class gsm_source_c(gr.hier_block2):
             [0,0,0],
         ]
         burst = sum(chunks,[])
-        burst = sum(map(list, zip(burst, (1,) * len(burst))), [])
+        burst = sum(list(map(list, list(zip(burst, (1,) * len(burst))))), [])
         burst += [1,0] * (l-148)
-        return map(int, burst)
+        return list(map(int, burst))
 
     def gen_gsm_frame(self):
         return \
@@ -186,7 +186,7 @@ class top_block(gr.top_block, pubsub):
         try:
             self._sink.get_sample_rates().start()
         except RuntimeError:
-            print "Sink has no sample rates (wrong device arguments?)."
+            print("Sink has no sample rates (wrong device arguments?).")
             sys.exit(1)
 
         # Set the clock source:
@@ -202,60 +202,60 @@ class top_block(gr.top_block, pubsub):
         if(options.gain):
             gain = self._sink.set_gain(options.gain)
             if self._verbose:
-                print "Set gain to:", gain
+                print("Set gain to:", gain)
 
         if self._verbose:
             gain_names = self._sink.get_gain_names()
             for name in gain_names:
                 range = self._sink.get_gain_range(name)
-                print "%s gain range: start %d stop %d step %d" % (name, range.start(), range.stop(), range.step())
+                print("%s gain range: start %d stop %d step %d" % (name, range.start(), range.stop(), range.step()))
 
         if options.gains:
             for tuple in options.gains.split(","):
                 name, gain = tuple.split(":")
                 gain = int(gain)
-                print "Setting gain %s to %d." % (name, gain)
+                print("Setting gain %s to %d." % (name, gain))
                 self._sink.set_gain(gain, name)
 
         if self._verbose:
             rates = self._sink.get_sample_rates()
-            print 'Supported sample rates %d-%d step %d.' % (rates.start(), rates.stop(), rates.step())
+            print('Supported sample rates %d-%d step %d.' % (rates.start(), rates.stop(), rates.step()))
 
         # Set the antenna
         if self._verbose:
-            print "setting antenna..."
+            print("setting antenna...")
         if(options.antenna):
             ant = self._sink.set_antenna(options.antenna, 0)
             if self._verbose:
-                print "Set antenna to:", ant
+                print("Set antenna to:", ant)
         try:
             self.publish(FREQ_RANGE_KEY, self._sink.get_freq_range)
         except:
-            print "Couldn't publish %s" % FREQ_RANGE_KEY
+            print("Couldn't publish %s" % FREQ_RANGE_KEY)
 
         try:
             for name in self.get_gain_names():
                 self.publish(GAIN_RANGE_KEY(name), (lambda self=self,name=name: self._sink.get_gain_range(name)))
         except:
-            print "Couldn't publish %s" % FREQ_RANGE_KEY
+            print("Couldn't publish %s" % FREQ_RANGE_KEY)
 
         try:
             self.publish(BWIDTH_RANGE_KEY, self._sink.get_bandwidth_range)
         except:
             if self._verbose:
-                print "Couldn't publish %s" % BWIDTH_RANGE_KEY
+                print("Couldn't publish %s" % BWIDTH_RANGE_KEY)
 
         try:
             for name in self.get_gain_names():
                 self.publish(GAIN_KEY(name), (lambda self=self,name=name: self._sink.get_gain(name)))
         except:
             if self._verbose:
-                print "Couldn't publish GAIN_KEYs"
+                print("Couldn't publish GAIN_KEYs")
         try:
             self.publish(BWIDTH_KEY, self._sink.get_bandwidth)
         except:
             if self._verbose:
-                print "Couldn't publish %s" % BWIDTH_KEY
+                print("Couldn't publish %s" % BWIDTH_KEY)
 
     def get_gain_names(self):
         return self._sink.get_gain_names()
@@ -277,7 +277,7 @@ class top_block(gr.top_block, pubsub):
             return True # Waveform not yet set
 
         if self._verbose:
-            print "Set sample rate to:", sr
+            print("Set sample rate to:", sr)
 
         return True
 
@@ -286,27 +286,27 @@ class top_block(gr.top_block, pubsub):
             g = self[GAIN_RANGE_KEY(name)]
             gain = float(g.start()+g.stop())/2
             if self._verbose:
-                print "Using auto-calculated mid-point gain"
+                print("Using auto-calculated mid-point gain")
             self[GAIN_KEY(name)] = gain
             return
 
         gain = self._sink.set_gain(gain, name)
         if self._verbose:
-            print "Set " + name + " gain to:", gain
+            print("Set " + name + " gain to:", gain)
 
     def set_bandwidth(self, bw):
         try:
             clipped_bw = self[BWIDTH_RANGE_KEY].clip(bw)
         except:
             if self._verbose:
-                print "couldn't clip bandwidth"
+                print("couldn't clip bandwidth")
             return
 
         if self._sink.get_bandwidth() != clipped_bw:
             bw = self._sink.set_bandwidth(clipped_bw)
 
             if self._verbose:
-                print "Set bandwidth to:", bw
+                print("Set bandwidth to:", bw)
 
     def set_dc_offset(self, value):
         correction = complex( self[DC_OFFSET_REAL], self[DC_OFFSET_IMAG] )
@@ -315,9 +315,9 @@ class top_block(gr.top_block, pubsub):
             self._sink.set_dc_offset( correction )
 
             if self._verbose:
-                print "Set DC offset to", correction
+                print("Set DC offset to", correction)
         except RuntimeError as ex:
-            print ex
+            print(ex)
 
     def set_iq_balance(self, value):
         correction = complex( self[IQ_BALANCE_MAG], self[IQ_BALANCE_PHA] )
@@ -326,16 +326,16 @@ class top_block(gr.top_block, pubsub):
             self._sink.set_iq_balance( correction )
 
             if self._verbose:
-                print "Set IQ balance to", correction
+                print("Set IQ balance to", correction)
         except RuntimeError as ex:
-            print ex
+            print(ex)
 
     def set_freq(self, freq):
         if freq is None:
             f = self[FREQ_RANGE_KEY]
             freq = float(f.start()+f.stop())/2.0
             if self._verbose:
-                print "Using auto-calculated mid-point frequency"
+                print("Using auto-calculated mid-point frequency")
             self[TX_FREQ_KEY] = freq
             return
 
@@ -343,22 +343,22 @@ class top_block(gr.top_block, pubsub):
         if freq is not None:
             self._freq = freq
             if self._verbose:
-                print "Set center frequency to", freq
+                print("Set center frequency to", freq)
         elif self._verbose:
-            print "Failed to set freq."
+            print("Failed to set freq.")
         return freq
 
     def set_freq_corr(self, ppm):
         if ppm is None:
             ppm = 0.0
             if self._verbose:
-                print "Using frequency corrrection of", ppm
+                print("Using frequency corrrection of", ppm)
             self[FREQ_CORR_KEY] = ppm
             return
 
         ppm = self._sink.set_freq_corr(ppm)
         if self._verbose:
-            print "Set frequency correction to:", ppm
+            print("Set frequency correction to:", ppm)
 
     def set_waveform_freq(self, freq):
         if self[TYPE_KEY] == analog.GR_SIN_WAVE:
@@ -433,24 +433,24 @@ class top_block(gr.top_block, pubsub):
         self.unlock()
 
         if self._verbose:
-            print "Set baseband modulation to:", waveforms[type]
+            print("Set baseband modulation to:", waveforms[type])
             if type == analog.GR_SIN_WAVE:
-                print "Modulation frequency: %sHz" % (n2s(self[WAVEFORM_FREQ_KEY]),)
-                print "Initial phase:", self[WAVEFORM_OFFSET_KEY]
+                print("Modulation frequency: %sHz" % (n2s(self[WAVEFORM_FREQ_KEY]),))
+                print("Initial phase:", self[WAVEFORM_OFFSET_KEY])
             elif type == "2tone":
-                print "Tone 1: %sHz" % (n2s(self[WAVEFORM_FREQ_KEY]),)
-                print "Tone 2: %sHz" % (n2s(self[WAVEFORM2_FREQ_KEY]),)
+                print("Tone 1: %sHz" % (n2s(self[WAVEFORM_FREQ_KEY]),))
+                print("Tone 2: %sHz" % (n2s(self[WAVEFORM2_FREQ_KEY]),))
             elif type == "sweep":
-                print "Sweeping across %sHz to %sHz" % (n2s(-self[WAVEFORM_FREQ_KEY]/2.0),n2s(self[WAVEFORM_FREQ_KEY]/2.0))
-                print "Sweep rate: %sHz" % (n2s(self[WAVEFORM2_FREQ_KEY]),)
+                print("Sweeping across %sHz to %sHz" % (n2s(-self[WAVEFORM_FREQ_KEY]/2.0),n2s(self[WAVEFORM_FREQ_KEY]/2.0)))
+                print("Sweep rate: %sHz" % (n2s(self[WAVEFORM2_FREQ_KEY]),))
             elif type == "gsm":
-                print "GSM Burst Sequence"
-            print "TX amplitude:", self[AMPLITUDE_KEY]
+                print("GSM Burst Sequence")
+            print("TX amplitude:", self[AMPLITUDE_KEY])
 
     def set_amplitude(self, amplitude):
         if amplitude < 0.0 or amplitude > 1.0:
             if self._verbose:
-                print "Amplitude out of range:", amplitude
+                print("Amplitude out of range:", amplitude)
             return False
 
         if self[TYPE_KEY] in (analog.GR_SIN_WAVE, analog.GR_CONST_WAVE, analog.GR_GAUSSIAN, analog.GR_UNIFORM):
@@ -466,7 +466,7 @@ class top_block(gr.top_block, pubsub):
             return True # Waveform not yet set
 
         if self._verbose:
-            print "Set amplitude to:", amplitude
+            print("Set amplitude to:", amplitude)
         return True
 
 def get_options():
@@ -525,19 +525,19 @@ def get_options():
 # the below does not run.
 def test_main():
     if gr.enable_realtime_scheduling() != gr.RT_OK:
-        print "Note: failed to enable realtime scheduling, continuing"
+        print("Note: failed to enable realtime scheduling, continuing")
 
     # Grab command line options and create top block
     try:
         (options, args) = get_options()
         tb = top_block(options, args)
 
-    except RuntimeError, e:
-        print e
+    except RuntimeError as e:
+        print(e)
         sys.exit(1)
 
     tb.start()
-    raw_input('Press Enter to quit: ')
+    input('Press Enter to quit: ')
     tb.stop()
     tb.wait()
 
