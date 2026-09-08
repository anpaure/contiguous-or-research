# Endpoint-orientation Boolean cuts for strict balanced expansion

Date: 2026-07-31  
Status: exact fixed-forest theorem, exact one-component flip criterion, and
independently replayed `n=3,4` finite obstruction/positive fixture.  No
all-parameter orientation theorem is claimed.

## 0. Result and scope

Fix the **unoriented** spanning Catalan path forest `F`.  Its two direct
occurrence multigraphs are already fixed: reversing any path changes neither
occurrence graph.  A coherent orientation chooses only which terminal endpoint
of every path receives weight one on each strict-balanced-expansion (SBE)
shore; the two shores choose opposite endpoints.

Consequently simultaneous upper/lower SBE is exactly one signed Boolean
endpoint-cut system.  Each cut is a threshold in path-orientation variables
with coefficients in `{-1,0,1}`.  Reversing one path changes every scaled SBE
slack by exactly one of `-C,0,C`, giving an exact one-flip repair test.

This clean reduction does **not** make the orientation problem integral.  On
the authenticated `n=3` forest, the half-endpoint point satisfies every upper
and lower SBE inequality, but no one of the `2^5` coherent orientation
bitstrings does.  The endpoint-matching form has the sharp two-block
obstruction

\[
             p(\{19\})+p(\{49\})=2>1,
\]

where `19--49` is one path-endpoint edge.  Its canonical in-cut demand also
fails crossing supermodularity.  Thus neither half-endpoint rounding nor a
direct application of the crossing-supermodular orientation theorem closes
the gate.

On the authenticated `n=4` forest, exactly `7600/2^14` stored-orientation
bitstrings satisfy both shores.  Four paths are singletons, so this is
`475/1024` distinct endpoint states, each repeated sixteen times.  Either one
of two individual path reversals repairs the stored orientation.

Everything below concerns SBE for one fixed unoriented structural forest.  It
does not choose a common basis `Q`, side representatives, a rooted graphic
base, the independent `c`-rail filler, residence, shadows, or a compiler.

## 1. Fixed occurrence graphs and complementary terminal banks

Use the standard parameters

\[
 M={2n\choose n},\qquad N={2n\choose n-1},\qquad
 P={2n\choose n-2},\qquad C=M-P,
 \qquad R=N-C,
\]

so the spanning path forest has `K=M-N` components.  Write component `i` as

\[
             P_i=(a_i,\ldots,b_i).
\]

Singleton paths are allowed, in which case `a_i=b_i`.  Introduce a Boolean
`x_i`: for `x_i=0` orient `P_i` from `a_i` to `b_i`, and for `x_i=1` reverse
it.  The upper strict occurrence graph uses the tail image and therefore
omits the final endpoint; the lower graph uses the head image and omits the
initial endpoint.  Put

\[
\begin{array}{c|cc}
&x_i=0&x_i=1\\ \hline
z_i^{\rm up}&b_i&a_i\\
z_i^{\rm lo}&a_i&b_i.
\end{array}                                             \tag{1.1}
\]

Thus `Z^up(x)={z_i^up(x)}` and `Z^lo(x)={z_i^lo(x)}` are complementary at
every nontrivial component and identical at a singleton component.

### Proposition 1.1 (orientation independence)

The upper and lower direct occurrence multigraphs depend only on the
unoriented forest `F`, not on `x`.

#### Proof

For a child edge `q={t_q,h_q}`, every candidate occurrence is defined from

\[
             L_q=t_q\cap h_q,\qquad U_q=t_q\cup h_q
\]

and an added or deleted coordinate.  Reversing a component swaps `t_q,h_q`
on all its edges but fixes `L_q,U_q`, the underlying edge `q`, and hence every
labelled occurrence `(q,x)`.  Only the tail/head puncture images change.
\(\square\)

This is why orientation is a terminal-bank variable, not a `Q`-selection or
occurrence-graph variable.

## 2. Exact signed Boolean cut system

Let (G_s=(O_s,X)) be either fixed occurrence graph, where
(s\in\{\mathrm{up},\mathrm{lo}\}).  For an outer family
(\mathcal A\subseteq O_s), put

\[
 B_s(\mathcal A)=N_{G_s}(\mathcal A),\qquad
 d_s(\mathcal A)=N|\mathcal A|-R|B_s(\mathcal A)|,
\]

and define its integral terminal demand

\[
 \theta_s(\mathcal A)=\max\left\{0,
       \left\lceil {d_s(\mathcal A)\over C}\right\rceil\right\}. \tag{2.1}
\]

### Theorem 2.1 (endpoint-cut normal form)

Orientation `x` makes shore `s` SBE if and only if

\[
       |B_s(\mathcal A)\cap Z^s(x)|\ge \theta_s(\mathcal A)
                 \qquad(\mathcal A\subseteq O_s).       \tag{2.2}
\]

For each component set

\[
 \alpha^0_{s,i}(\mathcal A)=1[z_i^s(0)\in B_s(\mathcal A)],\qquad
 \alpha^1_{s,i}(\mathcal A)=1[z_i^s(1)\in B_s(\mathcal A)].
\]

Then (2.2) is exactly

\[
 \sum_i\alpha^0_{s,i}(\mathcal A)
 +\sum_i\bigl(\alpha^1_{s,i}(\mathcal A)-\alpha^0_{s,i}(\mathcal A)\bigr)x_i
 \ge \theta_s(\mathcal A),                            \tag{2.3}
\]

whose variable coefficients lie in `{-1,0,1}`.  Simultaneous two-shore SBE
is the union of the two systems (2.3), with the **same** variables `x_i` and
the complementary convention (1.1).

#### Proof

The scaled SBE right side at cut \(\mathcal A\) is

\[
\begin{aligned}
 R|B_s(\mathcal A)\setminus Z^s(x)|+N|B_s(\mathcal A)\cap Z^s(x)|
 &=R|B_s(\mathcal A)|+(N-R)|B_s(\mathcal A)\cap Z^s(x)|\\
 &=R|B_s(\mathcal A)|+C|B_s(\mathcal A)\cap Z^s(x)|.
\end{aligned}
\]

Comparison with \(N|\mathcal A|\), followed by integral rounding, gives (2.2).  Expanding
the chosen endpoint of each component gives (2.3).  A singleton has
`alpha^0=alpha^1`, so its formal orientation bit cancels. \(\square\)

### Corollary 2.2 (sharp cut-local trichotomy)

For a fixed cut let `c_2,c_1,c_0` count path components for which both,
exactly one, or neither endpoint lies in \(B_s(\mathcal A)\).  Its terminal count ranges
exactly from `c_2` to `c_2+c_1`.  Therefore:

* if \(\theta_s(\mathcal A)\le c_2\), this cut holds for every orientation;
* if \(\theta_s(\mathcal A)>c_2+c_1\), no orientation can satisfy this cut;
* otherwise it is an at-least-\(\theta_s(\mathcal A)-c_2\) constraint on the `c_1`
  endpoint literals.

This is a complete single-cut obstruction/sufficiency statement.  Different
cuts can still request incompatible endpoint literals.

## 3. Exact one-path-flip calculus

Define the scaled slack

\[
 \Lambda_s(A;x)=R|B_s(A)|+C|B_s(A)\cap Z^s(x)|-N|A|.  \tag{3.1}
\]

For component `j`, let `x^j` be obtained by reversing only that component and
put

\[
 \delta_{s,j}(A;x)=
 1[z_j^s(1-x_j)\in B_s(A)]-1[z_j^s(x_j)\in B_s(A)].   \tag{3.2}
\]

Then `delta` belongs to `{-1,0,1}` and

\[
       \Lambda_s(A;x^j)=\Lambda_s(A;x)+C\delta_{s,j}(A;x). \tag{3.3}
\]

For \(\epsilon\in\{-1,0,1\}\) define

\[
 m_{s,j}^{\epsilon}(x)=
 \min\{\Lambda_s(A;x):\delta_{s,j}(A;x)=\epsilon\},   \tag{3.4}
\]

with the minimum of an empty class equal to `+infinity`.

### Theorem 3.1 (one-flip repair criterion)

Flipping component `j` makes shore `s` SBE if and only if

\[
       m_{s,j}^{+1}(x)\ge -C,\qquad
       m_{s,j}^{0}(x)\ge 0,\qquad
       m_{s,j}^{-1}(x)\ge C.                          \tag{3.5}
\]

It repairs both shores if and only if (3.5) holds for both `s=up,lo`.

#### Proof

Partition all cuts by their value of `delta` and substitute (3.3).  In the
three classes the post-flip inequalities are respectively old slack at least
`-C,0,C`. \(\square\)

In particular one flip cannot repair a deficit larger than `C`; every
currently violated cut must be a gain cut; and every losing cut must carry at
least `C` old slack.  These three necessary conditions are jointly sufficient.

## 4. Endpoint-matching orientation and failure of the Frank shortcut

Delete singleton components and make a matching `H` whose edges are the
nontrivial endpoint pairs `a_i b_i`, oriented from path initial endpoint to
path final endpoint.  For an endpoint trace `S` write `i_H(S)` for internal
matching edges and `rho_H(S)` for edges entering `S`.  Then

\[
 |Z^{\rm up}\cap B|
 = |B\cap Z_{\rm singleton}|+i_H(S)+\rho_H(S),        \tag{4.1}
\]

where \(S=B\cap V(H)\).  On the lower shore, chosen terminals are tails, so

\[
 |Z^{\rm lo}\cap B|
 = |B\cap Z_{\rm singleton}|+i_H(S)+\rho_H(V(H)\setminus S). \tag{4.2}
\]

Thus all cuts can be aggregated as lower bounds `rho_H(S)>=p(S)`.  If one
first closes the equivalent selected-head demands upward under subset
containment and then subtracts `i_H(S)`, one gets a canonical proof-safe
in-cut demand `p`.  Ordinary crossing-supermodular orientation theory would
apply only if this `p` had the required crossing-supermodularity and partition
properties.  It need not.

### Theorem 4.1 (conditional Frank/rounded-half route)

Suppose the canonical demand \(p:2^{V(H)}\to\mathbb Z_{\ge0}\), with
\(p(\varnothing)=p(V(H))=0\), is crossing
(H)-supermodular:

\[
 p(A)+p(B)\le p(A\cap B)+p(A\cup B)
       +d_H(A\setminus B,B\setminus A)                \tag{4.3}
\]

whenever `A,B` cross.  Then the
standard Frank orientation theorem says that an orientation covering `p`
exists if and only if, for every partition
\(\mathcal P=\{V_1,\ldots,V_t\}\) of \(V(H)\), both

\[
 \sum_{i=1}^t p(V_i)\le e_H(\mathcal P),\qquad
 \sum_{i=1}^t p(V(H)\setminus V_i)\le e_H(\mathcal P) \tag{4.4}
\]

hold, where \(e_H(\mathcal P)\) counts matching edges joining distinct
parts.  Equivalently these are the partition and co-partition inequalities.

In particular, under (4.3), feasibility of the half-endpoint orientation
for the **rounded in-cut demand**,

\[
                 {1\over2}d_H(S)\ge p(S)
                 \qquad(S\subseteq V(H)),             \tag{4.5}
\]

implies an integral SBE orientation.

#### Proof of the implication

The Frank equivalence is the standard covering-orientation theorem under the
displayed hypothesis.  Under (4.5), every matching edge sends one-half unit
in each direction while already covering the **integer** demand `p`.  For a
partition, an edge between two members contributes two halves to either the
partition sum or the complementary co-partition sum.  Hence

\[
 \sum_i p(V_i)
 \le {1\over2}\sum_i d_H(V_i)=e_H(\mathcal P),
\]

and the same calculation with `V(H)\setminus V_i` proves the second
inequality in (4.4).

Thus (4.4) holds and Frank gives an integral orientation. \(\square\)

The theorem is a useful positive criterion, but both its supermodularity
hypothesis and (4.5) are real extra conditions.  In particular, the raw
half-endpoint point `x_i=1/2` may satisfy every unrounded weighted-Hall row
without satisfying (4.5): taking a ceiling in the projected integer demand
can turn a positive fraction into demand one.  Proposition 4.2 exhibits
exactly this gap.

### Proposition 4.2 (smallest audited integrality obstruction)

For the authenticated `n=3` forest, the nontrivial endpoint matching is

\[
       (19,49),\quad(13,28),\quad(37,41),              \tag{4.6}
\]

and the singleton endpoints are `26,38`.  Exact lower-shore cuts imply

\[
                    p(\{19\})=p(\{49\})=1.            \tag{4.7}
\]

Only the matching edge `19--49` can enter either singleton block, and one
orientation cannot enter both.  Extending the two singleton blocks by the
remaining endpoint bank gives the violated partition inequality

\[
                 2=p(\{19\})+p(\{49\})>1,             \tag{4.8}
\]

proving integral infeasibility.

Moreover, in endpoint order

\[
                   (13,19,28,37,41,49),
\]

the canonical subset-closed in-cut demand has

\[
\begin{array}{c|cccc}
S& A=\{13,19\}&B=\{13,28\}&A\cap B&A\cup B\\ \hline
p(S)&1&0&0&0.
\end{array}                                            \tag{4.9}
\]

The sets `A,B` cross, so (4.9) violates
\(p(A)+p(B)\le p(A\cap B)+p(A\cup B)\).  Finally the half-endpoint vector
`x_i=1/2` satisfies every exact upper and lower weighted Hall cut.  It is
therefore a literal fractional-feasible/integer-infeasible instance.

The failure persists in the graph-corrected **positive** form required by
(4.3).  With

\[
 A'=\{19,37\},\qquad B'=\{28,37\},
\]

the audit gives

\[
 p(A')=p(B')=1,quad p(A'\cap B')=0,quad
 p(A'\cup B')=1,quad
 d_H(A'\setminus B',B'\setminus A')=0.               \tag{4.10}
\]

Thus the left side of (4.3) is `2` and the right side is `1`.  Moreover,
the raw half-SBE point gives only one-half unit entering each of the singleton
blocks in (4.7), whereas their rounded demands are one.  Hence both (4.3)
and the strong rounded-half condition (4.5) fail at `n=3`; raw half-SBE alone
cannot trigger Theorem 4.1.

The obstruction is not a failure of the SBE min-cut theorem; it is a failure
of integral correlation between complementary endpoint choices.  A different
lifted formulation might still be useful, but the raw endpoint demand is not
in the standard crossing-supermodular class.

## 5. Exact finite replay

The independent reconstruction

```text
scratch/audit_h2_catalan_sbe_endpoint_orientation_20260731.py
scratch/h2_catalan_sbe_endpoint_orientation_20260731.audit.json
```

loads the authenticated chained witness, rebuilds both occurrence graphs from
`L_q,U_q`, and enumerates only coherent component orientations.  It finds

\[
\begin{array}{c|c|c|c}
n&\text{orientation bitstrings}&\text{both-shore SBE}&
  \text{stored scaled violations (upper,lower)}\\ \hline
3&32&0&(11,4)\\
4&16384&7600&(14,0).
\end{array}                                            \tag{5.1}
\]

At `n=4`, flipping zero-based path `4`, with endpoints `(77,92)`, or path
`13`, with endpoints `(169,232)`, repairs the stored orientation.  The audit
also independently verifies (4.6)--(4.10) and zero twice-scaled **raw**
half-endpoint violation on both shores at `n=3` and `n=4`.

The separate independent cube replay

```text
scratch/independent_audit_catalan_sbe_orientation_cube_20260731.py
scratch/catalan_sbe_orientation_cube_20260731.independent.audit.json
```

agrees on `0/32`, `7600/16384`, the four singleton components, and the two
one-path repairs.  Freeze-time hashes are

```text
primary audit script
  dce22a41712caa7610135502bf3d7363873787832152a3bbdee82911b20df34c
primary audit JSON
  8079e1a838dafeeecef3e808e76c42cbb39e820c84237f8f7d73dcea94aad1c3
primary canonical payload
  9537e6ca587ce66a9fc5dedded1c209487203def7259eb3566cd55c0edd4c19d
independent audit script
  d3ea0aae711a14e0dc44a032ae20fe79bd9c914eb63e0966b93c6fb8b0abfefa
independent audit JSON
  7e604966b7e1f997a822d944b4fed80f78722d51cca0a3d15ef851abd5858d79
independent canonical payload
  8a8b81bdcd3567f3d19eb17b48a62be4d3ae15a0c74fb0a9c34510a0f250e6d7
```

At `n=4` the raw half point passes and integral orientations exist, but this
finite census does not prove that the rounded demand satisfies (4.5) or is
crossing `H`-supermodular.  It therefore supports, but does not prove, a
possible `n>=4` Frank-style threshold theorem.

## 6. Exact remaining gate

For a recursively supplied unoriented forest, SBE orientation is now exactly
the signed threshold system (2.3).  The right next theorem must control the
**joint endpoint-cut discrepancy** of its two fixed occurrence graphs.  It
cannot be replaced by:

1. choosing `Q` differently (the occurrence graphs and endpoint cuts precede
   `Q`);
2. checking the half-endpoint point (Proposition 4.2);
3. ordinary or graph-corrected positive crossing-supermodular orientation
   integrality (4.9)--(4.10); or
4. optimizing the independent `c`-rail filler, which is a separate quantified
   parent by the independent-filler theorem.

A valid all-parameter sufficient condition could instead prove that the
component-endpoint literals form a balanced/laminar special case, provide an
explicit discrepancy rounding with preservation margin, or export a bounded
endpoint-obstruction state through the recursion.  None is asserted here.

The conditional orientation statement used in Theorem 4.1 is the standard
Frank covering-orientation theorem; see András Frank,
[*On the orientation of graphs*](https://doi.org/10.1016/0095-8956(80)90071-4),
and the partition/co-partition formulation (Theorem 6.3) in András Frank and
Csaba Király,
[*Tree-compositions and orientations*](https://andrasfrank.web.elte.hu/cikkek/FrankJ64.pdf).
