# Audit correction: centered cyclic traces are not SCD-rotor cycles

Date: 2026-07-26

Audited file:

MATH_THEOREM_K_EXTENSIVE_C8_ONE_BASELINE_SHALLOW_PROFILE_GATE_20260726.md,
Section 5.

Method: pure mathematics only.

## 0. Verdict

The shallow repeat/hole ledger and action estimates outside Section 5 are
not addressed here.  Section 5's packet-to-rotor Lemma 5.1 is false for
the centered traces defined in its equation (5.1).  Consequently:

1. consecutive centered packet flags are not edges of the SCD central
   rotor graph;
2. Theorem 5.2's monotone-acyclicity proof does not apply to those packet
   flags; and
3. the prefix/suffix conclusions (5.9)--(5.10) do not follow from the
   claimed union of rotor cycles.

The intended monotone-SCD no-go is nevertheless true, with a stronger
linear exceptional-start bound.  In every ordinary packet, antipodal
starts have reversed depth-one chain words.  Hence a common-order
monotone SCD can contain at most \(m\) of the \(2m\) start flags.  For
\(K\) packets, at least

\[
 \boxed{mK={M\over2}=\left({1\over2}-o(1)\right)W}
\]

starts must be discarded.  This rules out the \(o(W/H)\)-exceptional BTK
coherence required by the one-baseline route.  It gives no obstruction to
a genuinely nonmonotone SCD.

## 1. Exact centered trace word

Let

\[
 \pi=(a_0,a_1,\ldots,a_{2m-1})
\]

be an ordinary cyclic order, with indices modulo \(2m\), and put

\[
 Z_t=\{a_t,a_{t+1},\ldots,a_{t+m-1}\}.
\]

Then

\[
 Z_{t+1}=Z_t-\{a_t\}+\{a_{t+m}\}.
\]

For \(1\le q\le d\), its centered lower and upper traces are

\[
 L_{q,t}=\bigcap_{i=0}^{q}Z_{t+i}
         =\{a_{t+q},\ldots,a_{t+m-1}\},
\]

\[
 U_{q,t}=\bigcup_{i=0}^{q}Z_{t+i}
         =\{a_t,\ldots,a_{t+m+q-1}\}.
\]

Read the corresponding symmetric chain segment upward:

\[
 L_{d,t}\subset\cdots\subset L_{1,t}\subset Z_t
 \subset U_{1,t}\subset\cdots\subset U_{d,t}.
\]

The labels added in this order are exactly

\[
 \boxed{
 w_t^{(d)}
 =(a_{t+d-1},a_{t+d-2},\ldots,a_t,
   a_{t+m},a_{t+m+1},\ldots,a_{t+m+d-1}).}
\tag{1.1}
\]

This word is forced by the sets themselves; it is not a decoration which
can be reordered while retaining the same SCD flag.

## 2. Failure of the rotor equation

At the next cyclic start,

\[
 w_{t+1}^{(d)}
 =(a_{t+d},a_{t+d-1},\ldots,a_{t+1},
   a_{t+m+1},\ldots,a_{t+m+d}).
\tag{2.1}
\]

An SCD rotor edge in the cited central graph would require

\[
 w_{t+1}^{(d)}
 =(x,w_{t,1}^{(d)},\ldots,w_{t,2d-1}^{(d)})
\tag{2.2}
\]

together with its endpoint equations.  Equations (1.1)--(2.1) do not
satisfy (2.2).  The failure is already visible at \(d=1\):

\[
 w_t^{(1)}=(a_t,a_{t+m}),\qquad
 w_{t+1}^{(1)}=(a_{t+1},a_{t+m+1}).
\]

Equation (2.2) would require the second entry of \(w_{t+1}^{(1)}\) to be
\(a_t\), impossible because all coordinates in the cyclic order are
distinct.

The source of the mismatch is conceptual.  The cyclic erosion compiler
represents the centered intersections and unions as unions of erosion
letters.  Its one-letter sliding chronology does not say that the
centered SCD chain word at start \(t+1\) is obtained by shifting the
centered SCD chain word at start \(t\).

Therefore Lemma 5.1 and every conclusion using that rotor projection must
be removed or explicitly replaced by a different state definition and a
new proof that it represents the same centered flags.

## 3. Correct monotone obstruction

At depth one, the antipodal start \(t+m\) has

\[
 w_{t+m}^{(1)}
 =(a_{t+m},a_{t+2m})=(a_{t+m},a_t),
\tag{3.1}
\]

the reverse of \(w_t^{(1)}\).

### Theorem 3.1 (antipodal reversal)

Suppose an SCD \(\mathcal D\) is monotone in one coordinate order
\(\ell\): every depth-one central word \((x,y)\) of \(\mathcal D\)
satisfies \(\ell(x)<\ell(y)\).  Then at most one of the two packet starts
\(t,t+m\) can be an original flag of \(\mathcal D\).

#### Proof

If the start \(t\) is coherent, (1.1) at \(d=1\) forces

\[
 \ell(a_t)<\ell(a_{t+m}).
\]

If \(t+m\) is coherent, (3.1) forces the reverse strict inequality.
They cannot both hold. \(\square\)

There are \(m\) disjoint antipodal pairs of starts in one packet.
Therefore at most \(m\) starts per packet can be coherent.  If a
\(K\)-packet family has \(M=2mK\) starts and becomes monotone-SCD
coherent after discarding \(s\), then

\[
 M-s\le mK,\qquad s\ge mK=M/2.
\tag{3.2}
\]

At \(q_0=\lceil m^{1/4}\rceil\),

\[
 M=N_{q_0}-\rho=(1-o(1))W,
\]

so (3.2) is the claimed \((1/2-o(1))W\) lower bound.  BTK and every
coordinate relabelling of BTK are common-order monotone, so this applies
to them.

## 4. Exact scope after correction

Certified:

* the centered trace formula (1.1);
* failure of the claimed rotor shift;
* invalidity of the rotor-cycle and derived prefix/suffix arguments for
  these traces; and
* the linear antipodal-reversal obstruction for every monotone SCD.

Not certified:

* any analogous obstruction for a nonmonotone SCD;
* extension of an arbitrary collision-free partial flag packing to one
  full SCD; or
* existence or nonexistence of an ECAP selection with aggregate
  \(o(W)\) shallow repeats.

Thus the correct surviving SCD gate is explicitly nonmonotone.
