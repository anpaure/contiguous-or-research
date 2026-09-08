# The minimal phase-coherent `K_(2,2)` aperture is a transporter, not a pump

**Date:** 2026-08-02  
**Status:** unconditional fixed-parent-cover theorem and sharp no-go for the
minimal four-edge/one-aperture face.  The statement includes the exact
cap/bi-history/private-edge correlation.  It does not rule out a
parent-native seed or a larger nonzero-holonomy actuator.

## 0. Verdict

The literal four-endpoint Pascal square cannot create the missing
child-native voltage.

Indeed, once all four old/crossed edges use one common choice of physical
endpoint lifts, their **integer** seam correction is zero.  If the two
opened child cycles have coherent integer totals `w_0,w_1`, then either
crossed edge may be retained as the private aperture, but every accepted
cap/history/closure tuple has the same closed total

\[
                              w_0+w_1.                 \tag{0.1}
\]

The cap and two history relations may reject one orientation or both.  They
cannot change (0.1).  Thus the accepted aperture relation has a constant
voltage coordinate; the minimal square supplies no closure-phase menu.

There is a useful positive transport consequence.  Two co-oriented copies
of lifted total `epsilon 2^a` produce `epsilon 2^(a+1)`, and one such copy
plus a zero companion preserves `epsilon 2^a`.  Every such total is a unit
modulo every odd, including composite, parent modulus.  This is a literal
transport theorem **provided the two parent-native input lifts already
exist**.  It is not a construction of those lifts from the old modulus.

Consequently the exact remaining child-native row cannot be discharged by
the minimal `K_(2,2)` aperture alone.  It needs either

1. one parent-native input whose total already has the required unit
   residue; or
2. a larger completed actuator with nonzero holonomy, or a private closure
   occurrence outside the common-lift square.

This obstruction is sharp: zero holonomy is exactly what makes the four
edges simultaneously realizable on the same four physical endpoint lifts.

## 1. Coherent integer-lifted ported children

Work in one parent cyclic cover with deck group `Z_N`.  For `i=0,1`, let

\[
 P_i:s_i\leadsto t_i,
 \qquad e_i:t_i\longrightarrow s_i                  \tag{1.1}
\]

be an oriented ported child.  Choose coherent integer representatives of
all path and seam gains, and put

\[
 p_i=\widetilde\delta(P_i),\qquad
 a_i=\widetilde\delta(e_i),\qquad
 w_i=p_i+a_i.                                         \tag{1.2}
\]

The integer representative is part of the recursive certificate.  Merely
changing one representative by a multiple of `N` is not an integer-coherent
dimension lift.

Let the Boolean port rectangle supply

\[
 f_{01}:t_0\longrightarrow s_1,
 \qquad f_{10}:t_1\longrightarrow s_0,               \tag{1.3}
\]

with integer gains `b_01,b_10`.

### Definition 1.1 (literal common-lift square)

The four seams form a literal common-lift square when there are integer
endpoint potentials `q(t_0),q(s_0),q(t_1),q(s_1)` such that

\[
\begin{aligned}
 a_i&=q(s_i)-q(t_i),\\
 b_{01}&=q(s_1)-q(t_0),\\
 b_{10}&=q(s_0)-q(t_1).
\end{aligned}                                         \tag{1.4}
\]

This is the integer refinement of the phase-coherent square.  Summing
(1.4) gives

\[
                  b_{01}+b_{10}=a_0+a_1              \tag{1.5}
\]

as an integer equality, not only modulo `N`.

Conversely, if the four displayed integer gains satisfy (1.5), fix
`q(t_0)=0`, set `q(s_0)=a_0`, then set

\[
 q(t_1)=a_0-b_{10},\qquad q(s_1)=q(t_1)+a_1.          \tag{1.6}
\]

Equation (1.5) verifies the remaining crossed edge.  Hence (1.5) is also
sufficient for one common system of integer endpoint lifts.

### Theorem 1.2 (trivial-stabilizer rail forces zero holonomy)

Let the four occurrence-labelled port arcs lie over one ordered rail `W`
under a cyclic action `G=Z_N`.  Put

\[
                         H=\operatorname{Stab}_G(W),   \tag{1.7}
\]

where the stabilizer fixes every block of the ordered rail in its displayed
position.  Choose left occurrence phases `ell_0,ell_1` and right role
phases `r_0,r_1` relative to one canonical copy of `W`.  With the port-arc
orientation convention used here, every literal arc gain has the form

\[
                         \delta_{ij}=\ell_i-r_j+h_{ij},
                         \qquad h_{ij}\in H.           \tag{1.8}
\]

Consequently the square holonomy satisfies

\[
 \delta_{01}+\delta_{10}-\delta_{00}-\delta_{11}
       =h_{01}+h_{10}-h_{00}-h_{11}\in H.             \tag{1.9}
\]

In particular, if `H={0}`, then every literal occurrence-labelled
`K_(2,2)` on the common rail is phase coherent automatically: its square
holonomy is zero in `G` and every one of its four arc gains is uniquely
forced in `G` by its two endpoint phases.  After choosing integer lifts of
the four endpoint phases and representing each arc gain by their integer
difference, the same alternating sum is exactly zero over the integers.

#### Proof

An arc from left occurrence `i` to right role `j` must identify their two
copies of the ordered rail.  Relative to the chosen canonical rail, the
required phase shift is `ell_i-r_j`; composing with an element of `H` is
the only ambiguity, which gives (1.8).  Taking the alternating `2 x 2`
sum cancels both left phases and both right phases and proves (1.9).  When
`H` is trivial, every `h_ij` vanishes in `G`.  Lifting the endpoint phases
to integers and taking their differences repeats the same cancellation
over `Z`, with no wrap ambiguity.  \(\square\)

For the pivot rail

\[
             W=(\{\rho_1\},\ldots,\{\rho_{d-1}\}),   \tag{1.10}
\]

the stabilizer is trivial whenever `d>=2`: a translation fixing even one
singleton coordinate is the identity.  Thus the literal pivot `K_(2,2)`
needs no additional phase-coherence choice.  At `d=1` the rail is empty
and this conclusion does not apply.

When `H` is nontrivial, rail alignment proves only zero holonomy in the
reduced phase group `G/H`.  The full-cover correction can be a nonzero
element of `H`; a proof-safe state must retain the stabilizer coset or the
complete phase-functional monodromy.  Treating (1.9) as zero in `G` would
be invalid.

## 2. Exact one-aperture relation

There are two possible crossed chronologies.  If `f_10` is the private
closing edge, the open word is

\[
                         P_0 f_{01} P_1               \tag{2.1}
\]

and closing it gives `P_0 f_01 P_1 f_10`.  If `f_01` is retained instead,
the open word is `P_1 f_10 P_0` and its closure is `f_01`.

Let `S` be the exact endpoint state space containing

* the cap current and prefix debt;
* the positive and negative directed histories, in the same physical
  frame; and
* every private-resource and topology field needed to certify the chosen
  closing edge.

For `r in {10,01}`, let `A_r` be the relation of all tuples

\[
             (x,y; f_r; z,b; w)                       \tag{2.2}
\]

for which the literal chronology with private closure `f_r`

1. maps endpoint state `x` to `y` in both directed-history relations;
2. has terminal cap current `z` and prefix debt `b`;
3. uses the displayed private closure occurrence and passes the declared
   topology/resource guards; and
4. has coherent integer closed total `w`.

This is a relation, not the Cartesian product of its marginals.

### Theorem 2.1 (constant-voltage fibre)

For a literal common-lift square,

\[
 \mathcal A_{10}\cup\mathcal A_{01}
   \subseteq
 S\times S\times\{f_{10},f_{01}\}
       \times\mathcal C_{\rm cap}\times\{w_0+w_1\}. \tag{2.3}
\]

In words, every cap/bi-history/private-edge accepted tuple has voltage
coordinate `w_0+w_1`.  This remains true if only one orientation is
accepted.

#### Proof

For the first orientation the integer total is

\[
\begin{aligned}
 p_0+b_{01}+p_1+b_{10}
 &= (p_0+a_0)+(p_1+a_1)\\
 &\quad +(b_{01}+b_{10}-a_0-a_1)\\
 &=w_0+w_1
\end{aligned}                                         \tag{2.4}
\]

by (1.5).  The second chronology contains the same four oriented fragments
and seams in cyclically shifted order, so it has the same sum.  Cap-prefix
and history acceptance inspect the corresponding literal word and may
remove tuples from `A_r`; neither operation changes the edge sum of a
surviving tuple.  The selected closure edge remains in (2.2), so no
independent marginalization has been used.  \(\square\)

### Corollary 2.2 (the minimal aperture has no phase menu)

If the output is opened at either crossed edge, its exact accepting
closure-total set is either empty or

\[
                         K_{\rm acc}=\{w_0+w_1\}.      \tag{2.5}
\]

Thus choosing which crossed edge survives can repair cap chronology or
history compatibility, but cannot tune the output voltage.

This strengthens the general aperture unit criterion on the minimal
square: here it reduces exactly to

\[
                         \gcd(N,w_0+w_1)=1.            \tag{2.6}
\]

### Corollary 2.3 (forced phase-labelled closure predicate)

On a trivial-stabilizer rail, once one crossed edge is designated as the
private aperture, its gain and its action on the coordinate-labelled
positive and negative histories are forced.  Hence membership in
`A_10` or `A_01` is an exact predicate on the supplied endpoint histories,
cap slack, and private edge; there is no residual deck-phase variable over
which to optimize.

This does **not** assert that the history relation has a unique fixed point.
It asserts that its phase-labelled transition map is unique.  Thus a failed
cap/history closure cannot be repaired by choosing another lift of the same
literal pivot port.

## 3. Dyadic transport and composite moduli

### Theorem 3.1 (literal dyadic doubling)

Suppose the two parent-native ported children have the same coherently
lifted total

\[
                         w_0=w_1=\epsilon 2^a,
       \qquad \epsilon\in\{-1,+1\}.                  \tag{3.1}
\]

If one of the two crossed chronologies is accepted in the exact sense of
Section 2, its exported aperture state has integer total

\[
                         \epsilon 2^{a+1}.             \tag{3.2}
\]

For every odd `N`, including composite `N`, this is a unit modulo `N`.

The asymmetric version with `w_1=0` transports `epsilon 2^a` unchanged.

#### Proof

Equation (3.2) is Theorem 2.1.  Every prime divisor of an odd integer is
odd, hence none divides a power of two.  The asymmetric assertion is the
same addition law.  \(\square\)

### Proposition 3.2 (doubling cannot repair coprimality)

For odd `N` and every integer `w`,

\[
                         \gcd(N,2w)=\gcd(N,w).         \tag{3.3}
\]

More generally, if an odd prime `p` divides `N,w_0,w_1`, then it also
divides every output of the minimal square.

#### Proof

Multiplication by two is a unit in `Z_N`, proving (3.3).  The second claim
follows from `p | (w_0+w_1)`.  \(\square\)

Thus two identical inherited copies cannot cure a new odd-prime obstruction
at a composite parent modulus.  In the same-parity step from modulus
thirteen to modulus fifteen, for example, an inherited integer total five
is a unit at the child, but two identical parent embeddings would have
total ten, still divisible by five at the parent.  Two unrelated units also
need not have unit sum: modulo nine, `1+2=3`.

## 4. Sharp pump obstruction

### Theorem 4.1 (no fresh pump on the minimal face)

Fix the two parent-native child paths and old closures.  Among all literal
common-lift `K_(2,2)` splices which retain exactly one crossed edge as the
private aperture and do not alter an input path internally, the output
voltage is forced to `w_0+w_1`.

Consequently such a splice cannot

1. turn two zero-voltage inputs into a generator;
2. remove a common prime divisor of the two input totals and `N`;
3. select a different dyadic residue by changing only which crossed edge
   is retained; or
4. repair a failed unit test by cap or bi-history postselection.

#### Proof

All claims follow from Theorem 2.1 and Proposition 3.2.  For item 4,
postselection only restricts the constant-voltage relation (2.3).
\(\square\)

The obstruction is sharp at the level of the four-edge geometry.  To add a
nonzero correction `eta`, one would need

\[
 b_{01}+b_{10}-a_0-a_1=\eta.                          \tag{4.1}
\]

But a common physical lift of the same four endpoints forces the left side
to be zero by (1.4).  Therefore a genuine pump must introduce at least one
of the following new resources:

* a parent-native input path whose total is already a unit;
* an additional phase-split endpoint occurrence or closure edge outside
  the common-lift square; or
* a larger completed nonzero-holonomy circuit which changes an input path
  before the zero-holonomy Pascal splice.

A formally nonzero integer correction equal to a multiple of `N` does not
change the parent residue and therefore is not a voltage pump.  Moreover,
changing one seam representative by `N` without changing the common
endpoint potentials destroys integer coherence and cannot be used as a
dimension-uniform certificate.

## 5. Exact product-monoid interface

The proof-safe minimal state is the correlated relation

\[
 \boxed{
 \mathfrak P=
  (\epsilon,a;\; z,b;\;\mathcal R_d^+,\mathcal R_d^-;
     f_{\rm ap};\;\mathcal P_{\rm priv}) ,}
                                                               \tag{5.1}
\]

where `epsilon 2^a` is the coherent integer total and the remaining fields
refer to the same literal chronology and closure occurrence.  At a binary
square, the voltage coordinate adds, the cap coordinate uses the exact
prefix product, and the two history relations compose along that same word.

For equal-sign dyadic inputs the phase update is simply

\[
                         (\epsilon,a)\mapsto
                         (\epsilon,a+1).               \tag{5.2}
\]

For a live input plus a neutral companion it is the identity.  Formula
(5.2) is constant-size structural state because the recursion level
determines `a`; it is not permission to choose cap, histories, or the
private edge independently.

Serial fixed-`z` completed tickets may follow this splice.  They preserve
(5.1) exactly only when their **complete** integer holonomy is zero, their
cap-prefix product is admitted, their two history relations return the
declared state, and they preserve the private aperture edge or export its
literal successor.

## 6. Minimal remaining lemma after the no-go

The minimal `K_(2,2)` face has now been decided: it transports a supplied
parent-native dyadic seed and preserves its exact correlation, but it
cannot generate that seed.

The next genuinely constructive lemma must therefore be one of the
following strictly stronger statements.

> **Parent-native dyadic input lemma.**  Before the Pascal square, realize
> one protected child path/closure in the parent cover with coherent total
> `epsilon 2^a`, while its cap/bi-history state and private closure edge are
> accepted by the same occurrence word.

or

> **Completed pump lemma.**  Realize a larger private actuator of nonzero
> holonomy `eta` whose cap current returns, whose positive and negative
> histories return to an accepted joint state, and whose private output
> aperture survives, with
> `w_0+w_1+eta=epsilon 2^a`.

The fixed-`z` zero-holonomy tickets are valid after either lemma, but cannot
substitute for it.  This is the exact minimal obstruction requiring a fresh
voltage pump; it is not a raw-abundance or component-count obstruction.

## 7. Scope

The theorem proves:

1. exact integer holonomy zero for the literal common-lift square;
2. automatic zero holonomy and forced phase-labelled arc maps on every
   trivial-stabilizer ordered rail, with the exact stabilizer-qualified
   correction otherwise;
3. the constant-voltage accepted aperture relation, including cap,
   bi-history, topology, and private-edge correlation;
4. dyadic transport and the full odd-composite coprimality audit; and
5. sharp impossibility of a fresh pump on the minimal four-edge face.

It does not construct a parent-native input seed, a completed nonzero-
holonomy actuator, ambient upper-shadow coverage, residence outside the
declared histories, source/envelope transport, or the terminal compiler.

## 8. Source chain

The fixed-cover voltage calculus and aperture unit criterion are in
`MATH_THEOREM_K_PASCAL_COPRIME_SEED_TRANSPORT_AND_APERTURE_VOLTAGE_GATE_20260802.md`.
The literal occurrence-labelled port square is in
`MATH_THEOREM_K_PASCAL_PORT_RECTANGLE_CALCULUS_AND_REGENERATIVE_BOX_GATE_20260802.md`.
The cap-prefix/history product and pivot state are in
`MATH_THEOREM_K_CAP_BACKUP_HISTORY_TICKET_MONOID_AND_HEPTAGON_HOST_GATE_20260802.md`
and
`MATH_THEOREM_K_DIRECTED_HISTORY_PORT_MONOID_AND_PIVOT_RESET_20260802.md`.
