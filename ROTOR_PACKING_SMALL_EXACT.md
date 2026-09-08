# First exact integral rotor-packing benchmark

The monotone-profile queue-packing gate is nonvacuous in its first
nontrivial instance.

For

\[
 m=3,\qquad h=1,\qquad H=2,
\]

there are ten queue atoms whose exposed chains partition every mask in the
three central ranks (2,3,4).  Thus

\[
 D_0=D_1^-=D_1^+=0.
\]

The queues and profiles are stored in
`scratch/verify_rotor_packing_m3.py`.  Each queue is a permutation giving

\[
 z_{-1},z_0,z_1,z_2,z_3,z_4,
\]

and each profile is `(d_0,d_1)`.  Direct enumeration checks all 50 required
masks, exact multiplicity one, monotonicity of every profile, and internal
disjointness of every atom.

`scratch/verify_rotor_packing_m3_factor.py` independently reconstructs the
canonical initialization and literal MTF update for every atom.  It verifies
that the ten factor words have total length 48 and that their literal suffix
ORs expose all 50 assigned masks.

The certificate contains six profiles `(1,1)`, three `(1,0)`, and one
`(0,0)`.  Hence its total number of depth-one states is

\[
 6\cdot2+3\cdot1=15=\binom62,
\]

while its twenty middle states equal (inom63).

This finite certificate does not prove the asymptotic packing lemma.  It is
the correct first regression test for any proposed general rounding or
decomposition theorem.

The verifier SHA-256 is

```text
a065ff2b05064df6e607cb157963166eb259dbf80a89f4544c87d863f6f41012
472deb93389bc73d179150b7814d7951d097b313d6d39f108be1504056aa4777
```
