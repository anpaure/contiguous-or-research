# Extensive \(C_8\) packets at the one-baseline scale: the exact shallow ledger, the fixed-frame obstruction, and the surviving SCD gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{0.1}
\]

and take the audited one-baseline scale

\[
 q_0=\lceil m^{1/4}\rceil,\qquad
 H=\lceil\sqrt{m\log m}\rceil.
\tag{0.2}
\]

Let

\[
 K=\left\lfloor {N_{q_0}\over2m}\right\rfloor,
 \qquad M=2mK=N_{q_0}-\rho,
 \qquad 0\le \rho<2m.
\tag{0.3}
\]

For any \(K\) literal ordinary cyclic packets, let \(C_0\) be their
middle repeat excess, let \(E_q\) be their lower depth-\(q\) repeat
excess, and let \(h_q\) be their lower depth-\(q\) hole count.  Upper
holes and repeats are equal to the lower ones by packetwise
complementation.  Then for every \(q<q_0\), exactly

\[
 \boxed{h_q=N_q-N_{q_0}+\rho+E_q.}
\tag{0.4}
\]

Consequently the complete shallow contribution to the literal
one-baseline word is

\[
 \boxed{
 2\sum_{q=1}^{q_0-1}h_q
 =\left({4\over3}+o(1)\right)Wm^{-1/4}
   +2\sum_{q=1}^{q_0-1}E_q.}
\tag{0.5}
\]

The deterministic first term is \(o(W)\).  Thus the exact shallow gate is

\[
 \boxed{C_0+2\sum_{q=1}^{q_0-1}E_q=o(W).}
\tag{0.6}
\]

Depthwise statements \(E_q=o(W)\) are insufficient because \(q_0\to
\infty\).  Exact shallow SCD-flag coherence makes every \(E_q\) and
\(C_0\) zero, and therefore passes (0.6).  More generally, coherence
outside \(s=o(W/H)\) starts is already sufficient, provided the same
good starts use one SCD through the annulus.

There is a genuine linear obstruction if one insists on one stationary
coordinate-pair frame.  For the exact fixed-frame type law, uniformly for
\(1\le q\le m^{1/4}\),

\[
 {D_{m,q}\over W}
 =\sqrt{2\over\pi}\,{q\over\sqrt m}
  +O\left({q^2\over m}+{1\over\sqrt m}\right),
\tag{0.7}
\]

where \(D_{m,q}\) is the forced lower hole count.  Hence

\[
 \boxed{
 2\sum_{q=1}^{q_0-1}D_{m,q}
   =\left(\sqrt{2\over\pi}+o(1)\right)W.}
\tag{0.8}
\]

This kills every one-fixed-frame shallow construction at the new scale.
It does **not** kill the cut MSW/extensive-\(C_8\) catalogue.  An ordinary
packet has its own antipodal matching, and the cut Catalan catalogue is
necessarily exponentially multi-frame.  In fact any packet family with
\(C_0=o(W)\) uses at least

\[
 \boxed{
 (1-o(1)){W\over2^m}
 \sim {2^m\over\sqrt{\pi m}}}
\tag{0.9}
\]

distinct antipodal frames.  The full canonical cut catalogue already
uses at least \(W/2^m\) frames.  Therefore applying (0.8) to ECAP* is a
quantifier error: the type \(f\) in the fixed-frame proof changes with
the packet.

The actual \(C_8\)-invariant is the orbit mass under the disjoint marked
coordinate swaps.  It gives an exact all-shallow overload functional,
proved below, but no present census forces that functional to be
\(\Omega(W)\) after optimizing the selected roots.  Thus:

> **Sharp boundary.** The shallow ledger does not refute ECAP*.
> Coherence with a monotone
> (in particular BTK) SCD is impossible even after deleting fewer than
> \((1/2-o(1))W\) starts.  The surviving SCD route must therefore use a
> genuinely nonmonotone SCD.  More generally the open problem is a coupled
> integral selection of complete shallow profiles, not a shortage of raw
> \(C_8\) action.

## 1. Normalization at \(q_0=m^{1/4}\)

The exact product formula gives, uniformly for \(q=o(\sqrt m)\),

\[
 {N_q\over W}
 =\prod_{i=1}^q{m-i+1\over m+i},\qquad
 \log {N_q\over W}=-{q^2\over m}
 +O\left({q^2\over m^2}+{q^4\over m^3}\right).
\tag{1.1}
\]

The ceiling in (0.2) therefore gives

\[
 {N_{q_0}\over W}
 =1-m^{-1/2}+O(m^{-3/4}).
\tag{1.2}
\]

Writing \(B=C_m=W/(m+1)\), one obtains

\[
 \boxed{
 {K\over B}
 ={m+1\over2m}{N_{q_0}\over W}+o(1)
 ={1\over2}-{1\over2\sqrt m}+O(m^{-3/4}).}
\tag{1.3}
\]

Thus the packet demand is just below one half of the Catalan rows.  The
audited extensive bank changes \(B-O(B/m)\) rows, so changed-row supply
has ample scalar slack: the gap \(B/2-K\sim B/(2\sqrt m)\) is much larger
than the \(O(B/m)\) inactive set.

The physical collar is also harmless:

\[
 2HK={H\over m}M
 =O\left(W\sqrt{{\log m}\over m}\right)=o(W).
\tag{1.4}
\]

## 2. The exact shallow repeat/hole identity

For a lower rank-\((m-q)\) target \(T\), let \(b_q(T)\) be the number of
selected packet starts having target \(T\).  Every one of the \(M\)
starts contributes once, so

\[
 \sum_Tb_q(T)=M.
\tag{2.1}
\]

Put

\[
 E_q=\sum_T(b_q(T)-1)_+,
 \qquad D_q=|\{T:b_q(T)>0\}|,
 \qquad h_q=N_q-D_q.
\tag{2.2}
\]

Since \(E_q=M-D_q\), one has for every \(0\le q<m\)

\[
 \boxed{h_q-E_q=N_q-M.}
\tag{2.3}
\]

At \(q=0\), \(N_0=W\), and the repeat excess is the middle collision
\(C_0=M-|\operatorname{supp}b_0|\).  For \(q<q_0\), substituting
\(M=N_{q_0}-\rho\) in (2.3) proves (0.4).  There is no probabilistic or
factor assumption in this identity.

For an ordinary cyclic packet, complementation takes the lower
length-\((m-q)\) intervals bijectively to the upper length-\((m+q)\)
intervals at antipodal starts.  Thus the two signed repeat and hole counts
are equal.  Concatenating the \(K\) erosion words, appending every missing
middle mask, and then appending every missing signed target through \(H\)
has exact displayed length

\[
 W+C_0+2HK+2\sum_{q=1}^{H}h_q.
\tag{2.4}
\]

Splitting at \(q_0\), (2.4) becomes

\[
\begin{aligned}
 W+2HK+C_0
 &+2\sum_{q=1}^{q_0-1}(N_q-N_{q_0}+\rho)
 +2\sum_{q=1}^{q_0-1}E_q\\
 &+2\sum_{q=q_0}^{H}h_q.
\end{aligned}
\tag{2.5}
\]

The audited uniform binomial expansion is

\[
 2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 ={W\over3m}(q_0-1)q_0(4q_0+1)
 +O\left(W{q_0^5+q_0^3\over m^2}\right).
\tag{2.6}
\]

Also \(2(q_0-1)\rho=O(m^{5/4})=o(W)\).  Equations
(2.5)--(2.6) prove (0.5), and prove the following exact criterion.

### Theorem 2.1 (one-baseline ECAP shallow gate)

A packet selection satisfying the annular ECAP condition

\[
 \sum_{q=q_0}^{H}h_q=o(W)
\tag{2.7}
\]

gives a central-through-\(H\) word of length \(W+o(W)\) if and only if

\[
 C_0+2\sum_{q=1}^{q_0-1}E_q=o(W).
\tag{2.8}
\]

Here “if and only if” refers to the explicit packet-plus-missing-target
compiler (2.4); accidental cross-seam witnesses can only improve the
unrestricted optimum.

## 3. Exact and approximate SCD-flag coherence

Let \(\mathcal D\) be an SCD of \(B_{2m}\), and let

\[
 \Omega=\mathcal D_{\ge q_0},\qquad |\Omega|=N_{q_0}.
\tag{3.1}
\]

Suppose the \(M\) packet starts are the original central flags of
\(M=N_{q_0}-\rho\) distinct chains in \(\Omega\).  At every
\(q<q_0\), distinct SCD chains have distinct rank-\((m-q)\) and
rank-\((m+q)\) members.  Their middle members are also distinct.  Hence

\[
 C_0=0,\qquad E_q^-=E_q^+=0\quad(1\le q<q_0).
\tag{3.2}
\]

If the states preserve the same SCD flags through the native radius and
through \(H\) when the chain reaches \(H\), then at any
\(q_0\le q\le H\) the unique SCD provider of a target is absent only if
one of the \(\rho\) omitted chains is its chain.  Therefore

\[
 h_q^- =h_q^+\le\rho,
 \qquad
 \sum_{q=q_0}^{H}(h_q^-+h_q^+)\le2(H-q_0+1)\rho=o(W).
\tag{3.3}
\]

Thus exact common-SCD flag coherence would imply the complete one-baseline
gate, with no shallow collision theorem left to prove.

The robust version is nearly as useful.

### Proposition 3.1 (exceptional-start stability)

Suppose that after discarding at most \(s\) packet starts, the remaining
starts are distinct flags of all but at most \(\rho+s\) chains of one
SCD, with the preceding coherence through \(H\).  Then the original
packet family satisfies

\[
 C_0\le s,\qquad E_q^\pm\le s\quad(q<q_0),
\tag{3.4}
\]

\[
 h_q^\pm\le\rho+s\quad(q_0\le q\le H).
\tag{3.5}
\]

In particular its non-deterministic central cost is at most

\[
 (4q_0+2H+O(1))s+2H\rho.
\tag{3.6}
\]

Thus \(s=o(W/H)\) is sufficient.

#### Proof

The coherent starts have load at most one at the middle and every shallow
rank.  Adding one exceptional start can increase repeat excess by at most
one at each rank, proving (3.4).  Removing \(s\) good starts omits at most
\(s\) additional SCD providers at each annular rank; putting the
exceptional starts back cannot create a hole.  This proves (3.5), and
summing the exact ledger proves (3.6). \(\square\)

## 4. A linear monotone-SCD obstruction

There is a tempting but incorrect argument that consecutive centered
packet flags form rotor edges of the SCD central-word graph.  They do
not.  If

\[
 Z_t=\{a_t,a_{t+1},\ldots,a_{t+m-1}\},
\tag{4.1}
\]

then the centered depth-\(d\) chain word, read from its bottom member to
its top member, is

\[
 w_t^{(d)}
 =(a_{t+d-1},a_{t+d-2},\ldots,a_t,
   a_{t+m},a_{t+m+1},\ldots,a_{t+m+d-1}).
\tag{4.2}
\]

Thus

\[
 w_{t+1}^{(d)}
 =(a_{t+d},\ldots,a_{t+1},
   a_{t+m+1},\ldots,a_{t+m+d}),
\tag{4.3}
\]

which is not of the rotor form
\((x,w_{t,1},\ldots,w_{t,2d-1})\).  Already at \(d=1\), a rotor would
require the second entry of \(w_{t+1}^{(1)}\) to equal \(a_t\), whereas it
is \(a_{t+m+1}\).  Therefore no prefix/suffix rotor cut may be applied to
these centered traces without a different state construction.

The correct monotone obstruction is simpler and much stronger.

### Theorem 4.1 (antipodal reversal obstruction)

Let \(\mathcal D\) be an SCD whose centered depth-one words are increasing
in one common coordinate order \(\ell\).  From each ordinary cyclic
packet, at most \(m\) of its \(2m\) centered start flags can be original
flags of \(\mathcal D\).  Consequently, if a \(K\)-packet family becomes
coherent with \(\mathcal D\) after discarding \(s\) starts, then

\[
 \boxed{s\ge mK={M\over2}
       =\left({1\over2}-o(1)\right)W.}
\tag{4.4}
\]

#### Proof

At depth one, (4.2) reads

\[
 w_t^{(1)}=(a_t,a_{t+m}).
\tag{4.5}
\]

The antipodal start \(t+m\) has

\[
 w_{t+m}^{(1)}=(a_{t+m},a_{t+2m})
               =(a_{t+m},a_t).
\tag{4.6}
\]

If both flags belonged to a common-order monotone SCD, (4.5) would force
\(\ell(a_t)<\ell(a_{t+m})\), while (4.6) would force the reverse
inequality.  Hence at most one start from each of the \(m\) antipodal
pairs can be coherent.  Summing over the \(K\) packets proves (4.4).
\(\square\)

The BTK/Greene--Kleitman SCD, and every coordinate relabelling of it, has
the required common-order monotonicity.  Since \(M=(1-o(1))W\), Theorem
4.1 rules out not only exact BTK coherence but also the
\(s=o(W/H)\)-exceptional coherence needed in Proposition 3.1.

This theorem is specific to monotone SCDs.  A nonmonotone SCD may orient
the two antipodal depth-one flags in opposite coordinate orders on
different chains.  No corresponding linear obstruction is proved for
all SCDs.

## 5. What one fixed pair frame would force

Fix one perfect matching \(\mathcal P\) of the \(2m\) coordinates.  In a
resolution whose transitions remain in this frame, a rank-\((m-q)\)
target is classified by its number \(f\) of full pairs.  The exact target
and source masses are

\[
 T_{f,q}
 ={m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q},
\tag{5.1}
\]

\[
 V_f={m!\over f!^2(m-2f)!}\,2^{m-2f}.
\tag{5.2}
\]

Type is preserved, so every such resolution, and every subresolution of
it, has at least

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+
\tag{5.3}
\]

lower holes.  The same holds above the middle.

### Theorem 5.1 (small-(q) fixed-frame deficit)

Uniformly for \(1\le q\le m^{1/4}\), equation (0.7) holds.

#### Proof

The likelihood ratio is exactly

\[
 {T_{f,q}\over V_f}
 =\prod_{i=0}^{q-1}{m-2f-i\over2(f+1+i)},
\tag{5.4}
\]

and is strictly decreasing in \(f\).  Write \(f=m/4+s\).  Uniformly for
\(|s|=O(q+1)\) and \(q\le m^{1/4}\), Taylor expansion of (5.4) gives

\[
 \log {T_{f,q}\over V_f}
 =-{8qs+3q^2+q\over m}
 +O\left({q^3\over m^2}+{q\over m^2}\right).
\tag{5.5}
\]

Consequently the last integer \(f_*(q)\) for which \(T_{f,q}>V_f\)
satisfies

\[
 f_*(q)={m\over4}-{3q+1\over8}+O(1).
\tag{5.6}
\]

Direct Stirling expansion of (5.1)--(5.2), uniformly in the central
\(O(\sqrt m)\) window, gives the corresponding distribution functions

\[
 \sum_{f\le f_*}{V_f\over W}
 =\Phi\left(-{3q\over2\sqrt m}\right)+O(m^{-1/2}),
\tag{5.7}
\]

\[
 \sum_{f\le f_*}{T_{f,q}\over N_q}
 =\Phi\left({q\over2\sqrt m}\right)+O(m^{-1/2}).
\tag{5.8}
\]

For completeness, the centers used here are

\[
 \mathbb E_V f={m\over4}-{1\over8}+O(m^{-1}),
\tag{5.9}
\]

\[
 \mathbb E_T f={m\over4}-{q\over2}-{1\over8}
                 +{q^2\over4m}+O(m^{-1}),
\tag{5.10}
\]

and both variances are \(m/16+O(q+1)\).  Equations (5.7)--(5.8) can also
be obtained by summing the central local Stirling formula; the tails
outside that window are exponentially small uniformly in the present
range.

Monotonicity of (5.4) now gives exactly

\[
 {D_{m,q}\over W}
 ={N_q\over W}\Pr_T(f\le f_*)-\Pr_V(f\le f_*).
\tag{5.11}
\]

Using

\[
 {N_q\over W}=1-{q^2\over m}+O\left({q^4+q^2\over m^2}\right)
\tag{5.12}
\]

and expanding \(\Phi\) at zero proves

\[
 {D_{m,q}\over W}
 ={2\over\sqrt{2\pi}}{q\over\sqrt m}
 +O\left({q^2\over m}+{1\over\sqrt m}\right),
\]

which is (0.7). \(\square\)

Summing Theorem 5.1 and using

\[
 {q_0^2\over\sqrt m}=1+o(1)
\tag{5.13}
\]

gives

\[
 \sum_{q=1}^{q_0-1}D_{m,q}
 =\left({1\over\sqrt{2\pi}}+o(1)\right)W.
\tag{5.14}
\]

Doubling for the two signs proves (0.8).  Notice the contrast with the
unavoidable SCD-simple shallow holes in (0.5): those cost only
\(O(Wm^{-1/4})\), whereas stationary pair type costs a positive multiple
of \(W\).

## 6. Why the fixed-frame theorem does not apply to cut MSW/\(C_8\) packets

For an ordinary cyclic order

\[
 \pi=(a_1,\ldots,a_{2m}),
\tag{6.1}
\]

define its antipodal frame

\[
 \mathcal P(\pi)=\{\{a_i,a_{i+m}\}:1\le i\le m\}.
\tag{6.2}
\]

Every length-\(m\) interval of \(\pi\) contains exactly one coordinate
from each pair of \(\mathcal P(\pi)\).  Thus all middle owners of one
packet are transversals of its own frame.  There are only \(2^m\)
transversals of one fixed frame.

### Proposition 6.1 (frame-diversity lower bound)

If a packet family \(\mathcal Q\) has \(M\) middle occurrences, middle
repeat excess \(C_0\), and uses \(R\) distinct antipodal frames, then

\[
 \boxed{M-C_0\le R2^m.}
\tag{6.3}
\]

In particular, at the scale (0.3), \(C_0=o(W)\) implies (0.9).

#### Proof

The distinct middle targets covered by packets having one fixed frame are
contained in that frame's \(2^m\) transversals.  Taking the union over
the \(R\) frames gives support at most \(R2^m\).  But middle support is
exactly \(M-C_0\). \(\square\)

The full cut Catalan catalogue has \(B\) rows whose nonwrapping primary
middle owners partition all \(W\) middle targets.  Every primary owner of
a row is a length-\(m\) interval and hence a transversal of that row's
antipodal frame.  Applying the same union bound to this partition shows

\[
 \#\{\mathcal P(\pi_x):x\in D_m\}\ge {W\over2^m}.
\tag{6.4}
\]

Thus exponential frame variation is present before any extensive switch
is made.

The reciprocal \(C_8\) move is also not a stationary-frame operation on
the cut packet.  In the local MSW block the two canonical orders begin

\[
 (4,2,3,1,T),\qquad(2,1,4,3,T),
\tag{6.5}
\]

and the switched orders begin

\[
 (4,3,2,1,T),\qquad(3,1,4,2,T).
\tag{6.6}
\]

After the root conjugation used by the completed factor, a fixed-root
packet changes the four labels inside one consecutive chronology block
while the outside order is fixed.  For \(m>4\), the antipodes of these
four consecutive positions lie outside the block; a nonidentity
permutation of the four labels therefore changes their matching partners
and hence changes \(\mathcal P(\pi)\).  Context insertion transports this
argument verbatim.  The extensive construction is a moving-frame
catalogue.

The fixed-frame identity (5.3) may be applied packetwise only after fixing
one common \(\mathcal P\) for all source strata.  Replacing
\(\mathcal P\) by \(\mathcal P(\pi)\) separately for every packet also
changes the meaning of \(f\); the type-orbit totals can no longer be
summed.  Equations (6.3)--(6.4) show that this is not a negligible
technicality but the essential exponential-scale feature of the cut
catalogue.

There is no pair-symmetry obstruction after unrestricted frame mixing at
the fractional level.  Indeed, for a fixed rank-\((m-q)\) target \(T\),
the number of perfect matchings in which \(T\) contains no full pair is

\[
 { (m+q)!\over 2^q q!}.
\tag{6.7}
\]

To see this, match the \(m-q\) elements of \(T\) injectively to
\(m-q\) elements of its complement, and then match the remaining \(2q\)
complement elements among themselves.  The count is independent of
\(T\).  Hence a uniform mixture of frames followed by a uniform
all-split target is uniform on the whole target layer.  This does not
construct an integral ECAP selection, but it proves that pair-frame
symmetry alone supplies no replacement for (5.3) once frames may vary.

## 7. The actual marked-swap orbit invariant

Let the extensive bank use disjoint coordinate transpositions

\[
 \Gamma=\langle\tau_1,\ldots,\tau_u\rangle\cong C_2^u.
\tag{7.1}
\]

For a certified rowwise packet \(c=(x,L)\), write

\[
 h_c=\prod_{j\in L}\tau_j,\qquad y_c=h_cx.
\tag{7.2}
\]

The completed-factor identity is

\[
 \pi_c=h_c\pi_{y_c}^{0}.
\tag{7.3}
\]

Fix a \(\Gamma\)-orbit \(O\) in the rank-\((m-q)\) target layer, and
define

\[
 a_{c,q}(O)=|E_{m-q}(\pi_{y_c}^{0})\cap O|.
\tag{7.4}
\]

Because \(h_c\in\Gamma\) permutes \(O\), equation (7.3) gives

\[
 |E_{m-q}(\pi_c)\cap O|=a_{c,q}(O).
\tag{7.5}
\]

For a selected packet multiset \(\mathcal Q\), put

\[
 A_{q,O}(\mathcal Q)=\sum_{c\in\mathcal Q}a_{c,q}(O).
\tag{7.6}
\]

### Theorem 7.1 (hereditary marked-orbit overload)

Every rowwise extensive-\(C_8\) selection obeys

\[
 \boxed{
 E_q\ge D_q^\Gamma(\mathcal Q)
 :=\sum_{O\in\binom{[2m]}{m-q}/\Gamma}
       (A_{q,O}(\mathcal Q)-|O|)_+.}
\tag{7.7}
\]

At the middle rank the same formula lower-bounds \(C_0\).  Consequently a
necessary condition for the one-baseline shallow gate is

\[
 \boxed{
 D_0^\Gamma(\mathcal Q)
 +2\sum_{q=1}^{q_0-1}D_q^\Gamma(\mathcal Q)=o(W).}
\tag{7.8}
\]

#### Proof

Equation (7.5) says that the total number of selected occurrences inside
\(O\) is exactly \(A_{q,O}\), independently of the local shore labels.
At most \(|O|\) of them can be distinct.  Therefore repeat excess inside
\(O\) is at least \((A_{q,O}-|O|)_+\).  Different orbits are disjoint, so
summing proves (7.7); summing over the shallow ranks proves (7.8).
\(\square\)

This is the correct coordinate-pair invariant for ECAP*.  It is finer
than merely saying that every available target lies in
\(\Gamma\mathcal V_q^0\), because it retains the complete occurrence
mass of each orbit.

It is not currently an obstruction theorem.  The orbit sizes and total
mass alone are compatible: since \(M<N_q\) for \(q<q_0\), the abstract
capacity system

\[
 0\le A_{q,O}\le|O|,\qquad \sum_OA_{q,O}=M
\tag{7.9}
\]

has both integral and fractional solutions.  In particular the
fractional uniform load \(M/N_q<1\) has zero overload.  What remains
unevaluated is whether the same \(K\) certified Catalan columns can realize
such orbit masses simultaneously at all shallow depths.  Any
\(\Omega(W)\) conclusion from (7.8) must therefore use the actual
root-orbit incidence matrix \(a_{c,q}(O)\), not only the abstract
wreath-product orbit sizes.

## 8. Root-scale action versus the full shallow profile

Take \(u=\lfloor\alpha m\rfloor\), \(0<\alpha<1/2\), and let
\(z_x=|J(x)|\) be the number of eligible reciprocal slots in root \(x\).
The exact Catalan moments are

\[
 \overline z={\alpha m\over8}+O_\alpha(1),\qquad
 {1\over B}\sum_x(z_x-\overline z)^2=O_\alpha(m).
\tag{8.1}
\]

At the new density (1.3), Cauchy--Schwarz gives, uniformly over every
set \(S\subseteq D_m\) with \(|S|=K\),

\[
 \boxed{
 \sum_{x\in S}z_x
 ={\alpha\over16}W+O_\alpha(W/\sqrt m).}
\tag{8.2}
\]

Thus the restricted one-variant-per-root ECAP* lane has genuine
root-scale eligible incidence supply on every admissible half-row shore;
it is not possible to make that supply disappear by choosing atypical
roots.

If \(I=\sum_{x\in S}|L_x|\) incidences are actually switched, the audited
locality bounds give

\[
 |C_0(\mathcal Q)-C_0(\mathcal Q^0)|\le2I,
\tag{8.3}
\]

\[
 |E_q(\mathcal Q)-E_q(\mathcal Q^0)|
 =|h_q(\mathcal Q)-h_q(\mathcal Q^0)|\le4I
 \quad(1\le q<m).
\tag{8.4}
\]

Therefore the entire shallow objective can move by at most

\[
 \boxed{
 \left|\Delta\left(C_0+2\sum_{q=1}^{q_0-1}E_q\right)\right|
 \le(8q_0-6)I
 \le\left({\alpha\over2}+o(1)\right)q_0W.}
\tag{8.5}
\]

This is an action **capacity**, not productive dispersion.  It is much
larger than the \(\Theta(W)\) aggregate fixed-frame deficit (0.8), so raw
action supply does not rule out repair.  On the other hand, the final
allowed objective is only \(o(W)\), and all \(q_0\) columns are tied to
the same local packet choices.  A separate choice at every depth is not
legal.

An exact robustness test is obtained by fixing a canonical \(K\)-root
set \(S\), putting \(I_S=\sum_{x\in S}z_x\), and defining its canonical
repeat profile \(C_0^0(S),E_q^0(S)\).  Every rowwise variant over \(S\)
satisfies

\[
\begin{aligned}
 C_0+2\sum_{q<q_0}E_q
 &\ge (C_0^0(S)-2I_S)_+\\
 &\quad+2\sum_{q<q_0}(E_q^0(S)-4I_S)_+.
\end{aligned}
\tag{8.6}
\]

Together, (7.8) and (8.6) are the present exact shallow obstruction
tests.  Neither has been evaluated to a positive multiple of \(W\) after
minimizing over \(S\).  Conversely, the existence of the action budget
(8.5) does not choose signs, avoid middle collisions, or produce one
common nested flag profile.

## 9. Certified boundary

The following statements are proved.

1. At \(q_0=\lceil m^{1/4}\rceil\), the deterministic two-sided shallow
   repair is \((4/3+o(1))Wm^{-1/4}=o(W)\).
2. The exact extra shallow cost is
   \(C_0+2\sum_{q<q_0}E_q\); aggregate, not merely depthwise, control is
   required.
3. Exact common-SCD flags make this extra cost zero, and
   \(o(W/H)\)-exceptional common-SCD coherence remains sufficient.
4. One stationary pair frame has the sharp two-sided aggregate deficit
   \((\sqrt{2/\pi}+o(1))W\).
5. That fixed-frame theorem is inapplicable to cut MSW/\(C_8\) packets:
   every low-middle-collision family is exponentially multi-frame.
6. Monotone-SCD coherence requires discarding at least
   \(M/2=(1/2-o(1))W\) packet starts, so it also rules out the
   \(o(W/H)\)-exceptional version.  Only a nonmonotone SCD can survive.
7. The actual marked-swap orbit overload (7.7)--(7.8) and the full-profile
   action bound (8.5)--(8.6) hold with their displayed constants.

The following statement remains open.

> Select \(K=\lfloor N_{q_0}/(2m)\rfloor\) certified extensive-\(C_8\)
> packets so that simultaneously
> \[
> C_0+2\sum_{q<q_0}E_q=o(W),\qquad
> \sum_{q=q_0}^{H}h_q=o(W),
> \]
> or, more strongly, embed all but \(o(W/H)\) of their starts into the
> coherent flags of one nonmonotone SCD.

No theorem here proves that selection, and no proved shallow invariant
rules it out.  This is the precise positive/negative boundary for the
extensive-\(C_8\) lane at the audited one-baseline scale.
