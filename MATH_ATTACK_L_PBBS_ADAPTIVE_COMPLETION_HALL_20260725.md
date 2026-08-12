# Lane L: adaptive open-wreath completion, exact Hall dual, and the cross-packet gate

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computation is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad W=\binom Nr,\qquad B_r=\frac WN=\operatorname{Cat}_r,
 \qquad H=\lceil \alpha\sqrt r\rceil,
\]

where \(\alpha>0\) is fixed. A simple return of gap \(2s+1\),
with \(s+1\le H\), has active halves

\[
 |U|=s,\qquad |A|=s+1,
\]

and inactive cores \(K,K'\), each of size

\[
 q=r-s.
\]

This report does **not** prove bounded adaptive congestion for every
projected-edge-disjoint Gaussian PBBS family, and therefore does not prove
the Catalan packing theorem or coefficient one. It proves the following
exact advances.

1. Tail completion is a path problem in one layered product-Boolean DAG.
   Its optimal fractional congestion has an exact min-cost-path dual. The
   constant dual weight already contains the Catalan cardinality theorem;
   generic Johnson expansion cannot bypass PBBS chronology.

2. One sector has exactly \(q\) pairwise tail-disjoint completions, and
   \(q\) is optimal. Thus local factorial freedom collapses to exactly
   \(q\) usable endpoint ports.

3. The two rank-\((r+1)\) endpoint owners give a composed fractional Hall
   routing through any \(b=O(\sqrt r)\) paired prefix layers with
   per-layer congestion at most

   \[
     4\exp\!\left(
      \frac{2b(H-1)+b(b+1)}{r-H-b+2}
     \right)
     \le 4e^{3\alpha^2+o_\alpha(1)}.
   \]

   The choices compose into actual prefix paths. Summing the layers still
   costs \(O_\alpha(\sqrt r)\); the missing saving is cross-time
   no-recycling.

4. There is an exact integral packet theorem. If the complementary core
   pairs of a fixed active packet lie in the sentinel-edge matching of one
   exact core wreath factor, then the whole packet has pairwise
   vertex-disjoint full ambient completions. The audited overlap-one
   zero-winding family satisfies this hypothesis for every fixed slot-size
   profile. The canonical MSW core factor gives full congestion one. More
   generally, a fractional cover by such packets of total weight \(D\)
   gives an adaptive fractional completion of congestion at most \(D\).

5. Uniform independent core orders are not the right final object. Even
   the Dyck sentinel matching has uniform reciprocal-binomial load

   \[
     (3-4\log2)q+O(1)
   \]

   at an explicit target, while its MSW adaptive completion has congestion
   one. More strongly, Section 8 constructs a genuine audited overlap-one
   PBBS packet in every fixed Gaussian window whose uniform tail load is
   \(\Omega_\alpha(\sqrt r)\). Thus the proposed uniform pointwise kernel
   bound is false; adaptive completion survives.

6. Genuine PBBS endpoints force the sharp prefix corridor

   \[
     |P\cap U|-|P\cap V|
     \ge\bigl||P\cap K|-|P\cap K'|\bigr|.
   \]

   Even this condition, endpoint-owner nonreuse, and disjoint fixed-core
   open traces allow an endpoint-compatible Gaussian family with adaptive
   congestion \(\Omega(q)\). It is not asserted to satisfy intermediate
   PBBS chronology.

7. On the unrestricted complementary-core family, the exact fractional
   cover number by congestion-one sentinel packets is \((q+1)/2\), while
   every adaptive assignment has congestion at least
   \((q+1)(2q-1)/(2(2q+1))\). Thus the packet reduction is asymptotically
   sharp, and generic fixed-core or endpoint Hall arguments necessarily
   lose order \(q\).

The exact remaining theorem is therefore a **cross-profile, cross-packet
adaptive no-recycling theorem** for the genuine PBBS simultaneous cyclic
ballot fibres. Local completion flexibility and independent uniform
completion are both exhausted.

## 1. Exact simple-sector coordinates

Write the simple omitted-label word as

\[
 a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s,a_0,
\]

where the half-open list through \(a_s\) is pairwise distinct. Put

\[
 U=\{b_0,\ldots,b_{s-1}\},
 \qquad
 A=\{a_0,\ldots,a_s\},
\]

and

\[
 R=[N]\setminus(A\cup U)=K\mathbin{\dot\cup}K'.
\]

The fixed open segment is

\[
 X_{2h}=K\cup\{a_0,\ldots,a_{h-1}\}
              \cup\{b_h,\ldots,b_{s-1}\},
 \tag{1.1}
\]

\[
 X_{2h+1}=K'\cup\{b_0,\ldots,b_{h-1}\}
                \cup\{a_{h+1},\ldots,a_s\},
 \tag{1.2}
\]

for \(0\le h\le s\). Its endpoints are

\[
 X_0=K\cup U,\qquad X_{2s+1}=K'\cup U.
 \tag{1.3}
\]

The complementary rank-\((r+1)\) endpoint owners are

\[
 L=A\cup K,
 \qquad
 R_+=A\cup K'.
 \tag{1.4}
\]

They have Johnson distance \(q\). This pair, rather than either endpoint
alone, is the natural state for adaptive completion.

## 2. Tail completion as one product-Boolean path

At level \(t\), \(0\le t\le q\), take states

\[
 (S,S'),\qquad S\subseteq K,\quad S'\subseteq K',
 \quad |S|=|S'|=t,
\]

representing the owner

\[
 P(S,S')=A\cup(K\setminus S)\cup S'.
 \tag{2.1}
\]

An arc

\[
 (S,S')\longrightarrow(S\cup\{k\},S'\cup\{k'\})
 \tag{2.2}
\]

chooses the next removed and inserted core labels. Thus source-to-sink
paths are in bijection with ordered pairs of permutations

\[
 k_1,\ldots,k_q\quad\hbox{of }K,
 \qquad
 k'_1,\ldots,k'_q\quad\hbox{of }K'.
\]

Put

\[
 P_i=A\cup\bigl(K\setminus\{k_1,\ldots,k_{i-1}\}\bigr)
       \cup\{k'_1,\ldots,k'_{i-1}\}.
\]

Then

\[
 P_{i+1}=P_i-\{k_i\}+\{k'_i\}.
\]

The exact middle tail states are

\[
 E_i=P_i\cap P_{i+1}=P_i\setminus\{k_i\},
 \qquad 1\le i\le q,
 \tag{2.3}
\]

and

\[
 O_i=P_{i+1}^{\,c},
 \qquad 1\le i\le q-1.
 \tag{2.4}
\]

The omitted endpoint complements

\[
 P_1^c=K'\cup U,
 \qquad
 P_{q+1}^c=K\cup U
\]

are exactly the two fixed open endpoints. Hence every tail has exactly

\[
 q+(q-1)=2q-1
 \tag{2.5}
\]

new vertices. Independent per-layer assignments are not enough: the
selected states must arise from one path in (2.2).

## 3. Exact fractional congestion dual

Let \(\Omega_I\) be the finite set of completion paths for sector \(I\),
and let \(H_I(\omega)\) be the \((2q_I-1)\)-vertex tail of path \(\omega\).
Define

\[
 C^*(\mathcal P)
 =\min_{\substack{\mu_{I,\omega}\ge0\\
                  \sum_{\omega\in\Omega_I}\mu_{I,\omega}=1}}
   \max_{T\in\binom{[N]}r}
   \sum_I\sum_{\omega\in\Omega_I}
      \mu_{I,\omega}\mathbf1_{\{T\in H_I(\omega)\}}.
 \tag{3.1}
\]

For nonnegative target weights \(y=(y_T)\), put

\[
 d_I(y)=\min_{\omega\in\Omega_I}
             \sum_{T\in H_I(\omega)}y_T.
 \tag{3.2}
\]

### Theorem 3.1 (chronology-preserving Farkas dual)

One has the exact identity

\[
 \boxed{
 C^*(\mathcal P)
 =\max_{\substack{y_T\ge0\\\sum_Ty_T=1}}
   \sum_{I\in\mathcal P}d_I(y).}
 \tag{3.3}
\]

Equivalently, \(C^*(\mathcal P)\le C\) if and only if

\[
 \boxed{
  \sum_I d_I(y)\le C\sum_Ty_T
  \quad\hbox{for every }y\ge0.}
 \tag{3.4}
\]

#### Proof

For fixed \(y\), minimizing the weighted load over the product of the
sector simplices separates by sector and gives the right side of (3.2).
Finite-dimensional minimax between the completion distributions and the
simplex of target weights gives (3.3). Homogeneity gives (3.4). All
minima in (3.2) are minimum-cost paths in the single DAG (2.2), so the dual
does not relax chronology. \(\square\)

The constant weight is already decisive. Since

\[
 d_I(\mathbf1)=2q_I-1
\]

and \(s_I+1\le H\) implies \(q_I\ge r-H+1\),

\[
 \sum_I(2q_I-1)\ge (N-2H)|\mathcal P|.
\]

Therefore

\[
 \boxed{
 C^*(\mathcal P)\le C
 \Longrightarrow
 |\mathcal P|
 \le\frac{CW}{N-2H}
 =C\bigl(1+O_\alpha(r^{-1/2})\bigr)B_r.}
 \tag{3.5}
\]

Thus bounded adaptive tail congestion already contains the Catalan-order
packing theorem in its all-ones cut. This explains why a black-box local
Hall theorem cannot settle the problem without using PBBS chronology.

## 4. The exact local rank is \(q\)

Choose cyclic orders

\[
 K=\{k_a:a\in\mathbb Z_q\},
 \qquad
 K'=\{k'_a:a\in\mathbb Z_q\}.
\]

For each \(a\), use the two linear orders beginning at \(a\). The resulting
tail states are

\[
 O_i^a
 =U\cup\{k_a,\ldots,k_{a+i-1}\}
   \cup\Bigl(K'\setminus\{k'_a,\ldots,k'_{a+i-1}\}\Bigr),
 \tag{4.1}
\]

for \(1\le i\le q-1\), and

\[
 E_i^a
 =A\cup\Bigl(K\setminus\{k_a,\ldots,k_{a+i-1}\}\Bigr)
   \cup\{k'_a,\ldots,k'_{a+i-2}\},
 \tag{4.2}
\]

for \(1\le i\le q\), with cyclic indices.

For fixed \(i<q\), the cyclic \(i\)-subsets of \(K\) distinguish the
\(q\) shifts. For \(E_q^a\), the missing singleton \(k'_{a-1}\)
distinguishes them. Different indices have different \(K\)-intersection
sizes. No \(E\)-state is an \(O\)-state because their active traces are
respectively \(A\) and \(U\). Hence the \(q\) shifted tails are pairwise
disjoint.

Conversely, every completion contains one of the \(q\) first states

\[
 \mathcal F_I
 =\{A\cup(K\setminus\{k\}):k\in K\}.
 \tag{4.3}
\]

Thus \(\mathcal F_I\) is a transversal of the tail-completion hypergraph.
The construction and transversal give

\[
 \boxed{
  \nu(\mathcal H_I)=\tau(\mathcal H_I)=q.}
 \tag{4.4}
\]

The factorial number \((q!)^2\) of completions therefore supplies exactly
\(q\), and no more than \(q\), mutually disjoint local choices.

## 5. Composed endpoint-prefix Hall flow

The tail obeys

\[
 O_i=E_i^c\setminus\{k'_i\},
 \qquad
 E_{i+1}=O_i^c\setminus\{k_{i+1}\}.
 \tag{5.1}
\]

We first record the one-step lemma.

### Lemma 5.1 (allowed-face assignment)

Suppose rank-\((r+1)\) owners carry total mass at most \(c\) per owner,
and every owner has at least \(h\) allowed deletions. There is a fractional
assignment to allowed rank-\(r\) faces with face load at most

\[
 \boxed{\frac{c(r+1)}h.}
 \tag{5.2}
\]

For integral tokens with owner multiplicity at most \(c\), there is an
integral assignment with face capacity

\[
 \boxed{\left\lceil\frac{c(r+1)}h\right\rceil.}
 \tag{5.3}
\]

#### Proof

Distribute each fractional owner mass uniformly among its allowed faces.
A fixed rank-\(r\) face has exactly \(r+1\) rank-\((r+1)\) supersets, which
proves (5.2). For integral tokens, the incidence graph has left degree at
least \(h\) and right degree at most \(c(r+1)\). Hence every left set
\(S\) has

\[
 h|S|\le c(r+1)|N(S)|.
\]

Clone each right vertex \(\lceil c(r+1)/h\rceil\) times and apply Hall.
\(\square\)

For a sector family, the complement of the first owner is a fixed open
endpoint. Open-segment throughput therefore gives initial owner
multiplicity at most four. Put

\[
 q_0=\min_Iq_I\ge r-H+1.
\]

For \(1\le b\le q_0-1\), iterating the fractional lemma through

\[
 E_1,O_1,\ldots,E_b,O_b
\]

gives a distribution on genuine composed prefix paths whose individual
layer loads are at most

\[
 c_{2b}
 \le4\prod_{i=1}^{b}
 \left(\frac{r+1}{q_0-i+1}\right)^2.
 \tag{5.4}
\]

Since \(q_0\ge r-H+1\),

\[
 \begin{aligned}
 \log\frac{c_{2b}}4
 &\le2\sum_{i=1}^b
  \frac{H+i-1}{r-H-b+2}\\
 &=\frac{2b(H-1)+b(b+1)}{r-H-b+2}.
 \end{aligned}
\]

Thus

\[
 \boxed{
 c_{2b}\le4\exp\!\left(
 \frac{2b(H-1)+b(b+1)}{r-H-b+2}
 \right).}
 \tag{5.5}
\]

If \(b,H\le\alpha\sqrt r\), then

\[
 \boxed{c_{2b}\le4e^{3\alpha^2+o_\alpha(1)}.}
 \tag{5.6}
\]

The total load summed over these \(2b\) layers is at most

\[
 \boxed{2b\,c_{2b}\le8b e^{3\alpha^2+o_\alpha(1)}.}
 \tag{5.7}
\]

The reverse endpoint gives the identical suffix theorem. The integral
one-step lemma composes with successive ceilings, but no constant bound is
claimed for that rounded recurrence. Equations (5.4)--(5.7) close the
per-layer Hall problem through a Gaussian prefix while retaining one actual
path. They do not prevent the same target from being used at many
different recursion times.

## 6. Sentinel contraction of one core factor

Adjoin a dummy coordinate \(\infty\) to the \(2q\)-set \(R\). For a
\(q\)-subset \(Q\subseteq R\cup\{\infty\}\), define

\[
 \Psi(Q)=
 \begin{cases}
  U\cup Q,&\infty\notin Q,\\
  A\cup(Q\setminus\{\infty\}),&\infty\in Q.
 \end{cases}
 \tag{6.1}
\]

### Theorem 6.1 (core-star contraction)

Let \(\mathcal F_q\) be an exact \((2q+1,q)\) wreath factor on
\(R\cup\{\infty\}\). Every row has a unique edge omitting \(\infty\);
its endpoints are complementary \(q\)-sets \(K,K'=R\setminus K\).
Suppose a fixed-active sector packet has one distinct sector for each of a
subfamily of these sentinel edges. Cut each selected core row at its
sentinel edge, apply \(\Psi\) to its vertices, and splice in the sector's
fixed open path (1.1)--(1.2). The resulting full ambient wreaths are
pairwise vertex-disjoint.

#### Proof

Orient a selected core row so that its omitted word is

\[
 \infty,k_1,k'_1,\ldots,k_q,k'_q.
\]

Cutting the \(\infty\)-edge gives a path between \(K\) and \(K'\). Its
internal vertices alternate between

\[
 \{\infty\}\cup(K\setminus\{k_1,\ldots,k_i\})
 \cup\{k'_1,\ldots,k'_{i-1}\}
\]

and

\[
 \{k_1,\ldots,k_i\}
 \cup(K'\setminus\{k'_1,\ldots,k'_i\}).
\]

Under \(\Psi\), these are exactly the states (2.3)--(2.4). The core row
has \(2q+1\) vertices; removing its two endpoints leaves \(2q-1\) new
tail vertices. The open path has \(2s+2\) vertices and shares precisely
the two endpoints. Hence the completed row has

\[
 (2q+1)+(2s+2)-2=2r+1=N
\]

vertices, and its omitted labels are the \(2q\) core labels and the
\(2s+1\) distinct active labels, each once. It is therefore a literal
exact wreath.

Distinct core-factor rows are vertex-disjoint, and \(\Psi\) is injective:
the active trace \(A\) or \(U\) recovers whether \(\infty\) was present.
Therefore the images of all core-row vertices, including the two
sentinel-edge endpoints, are disjoint across rows. This handles
tail--tail, tail--foreign-endpoint, and endpoint--endpoint collisions.
In (1.1), the active trace equals \(U\) only
at \(h=0\); in (1.2), it equals \(U\) only at \(h=s\). Every open trace
has size \(s\), whereas \(A\) has size \(s+1\). Hence an \(A\)-tail
cannot be open, and a \(U\)-tail can be open only at one of the two
endpoints. Those two residual sets were removed from the new tail.
The nonendpoint active traces in (1.1)--(1.2) determine their time index.
Thus equality between two internal open vertices would force equality of
their \(R\)-parts, \(K=K\) or \(K'=K'\); equality at the two endpoint
traces would force \(K_I=K'_J\) or the identical alternative. In every
case two distinct sectors would make two core-factor rows share a residual
vertex, impossible. Within one completed row, simplicity follows from
injectivity of \(\Psi\) and the \(2s+1\) distinct active omitted labels.
\(\square\)

This theorem is integral. It chooses one full literal wreath for every
sector and uses no signed or fractional relaxation.

### Lemma 6.2 (fractional cover by compatible sentinel packets)

Let \(\mathcal P\) be any sector family. Suppose \(\mathfrak M\) is a
collection of packets \(M\subseteq\mathcal P\), and for every
\(M\in\mathfrak M\) one has chosen one full completion
\(\mathcal H_{M,I}\) for each \(I\in M\), with

\[
 \sum_{I\in M}{\bf1}_{\{T\in\mathcal H_{M,I}\}}\le1
 \qquad\text{for every ambient target }T.
 \tag{6.2}
\]

Let \(w_M\ge0\) satisfy the fractional packet-cover inequalities

\[
 c_I:=\sum_{M\ni I}w_M\ge1
 \qquad(I\in\mathcal P).
 \tag{6.3}
\]

Then \(\mathcal P\) has a fractional adaptive full-completion assignment
of congestion at most

\[
 D:=\sum_{M\in\mathfrak M}w_M.
 \tag{6.4}
\]

In particular, (6.2) holds whenever each \(M\) is contained in the
sentinel-edge packet of one exact core factor and its completions are those
of Theorem 6.1.

#### Proof

For sector \(I\), choose packet \(M\ni I\) with probability
\(w_M/c_I\), and then use \(\mathcal H_{M,I}\). This is one distribution
on literal full wreaths because the probabilities sum to one. At a target
\(T\), its expected load is

\[
 \begin{aligned}
 \Lambda(T)
 &=\sum_I\sum_{M\ni I}\frac{w_M}{c_I}
       {\bf1}_{\{T\in\mathcal H_{M,I}\}}\\
 &\le \sum_Mw_M\sum_{I\in M}
       {\bf1}_{\{T\in\mathcal H_{M,I}\}}
 \le\sum_Mw_M=D.
 \end{aligned}
 \tag{6.5}
\]

No joint sampling or simultaneous disjoint realization is claimed across
different sectors. The common packet supplies the disjointness inequality
inside each term of the fractional load calculation. \(\square\)

Thus a bounded-weight fractional cover by core-factor-compatible packets
is a sufficient constructive form of the desired adaptive theorem. A
single common residual Dyck order is the special case \(D=1\).

## 7. A genuine PBBS packet with congestion one

Use the audited overlap-one zero-winding construction. For fixed \(s\),
choose Dyck words

\[
 S_0=S_s=\varnothing,
 \qquad \operatorname{ht}(S_j)\le\min(j,s-j),
\]

and

\[
 \operatorname{ht}(T_h)\le\min(h,s-1-h).
\]

Its normalized root has the form

\[
 D_0=
 \prod_{h=s-1}^{0}(\overline T_h1)\,
 \prod_{j=s-1}^{1}(0S_j)\,0.
 \tag{7.1}
\]

The displayed \(s\) ones and \(s+1\) zeros are the active coordinates.
Deleting them leaves the core membership word

\[
 \overline T_{s-1}\cdots\overline T_0
 S_{s-1}\cdots S_1.
 \tag{7.2}
\]

Fix all block semilengths. The active coordinate positions, and hence the
whole active omitted-label word, now depend only on those lengths, not on
the Dyck contents. Thus all choices form one fixed-active packet.

Reverse the coordinate order inside each \(T_h\)-block only. Then (7.2)
becomes

\[
 \mu(T_{s-1})\cdots\mu(T_0)
 S_{s-1}\cdots S_1,
 \qquad \mu(T)=\overline{\operatorname{rev}(T)}.
 \tag{7.3}
\]

Every factor in (7.3) is Dyck, so (7.3) is a Dyck word of semilength
\(q=r-s\). Fixed block boundaries recover all \(S_j,T_h\), so distinct
packet roots give distinct core sets \(K\).

The canonical MSW exact factor on \(R\cup\{\infty\}\) is indexed by Dyck
words \(x\). The row indexed by \(x\) has closing sentinel edge

\[
 x,\quad R\setminus x.
\]

Therefore all core pairs of the packet lie in the sentinel matching of
one MSW factor. Theorem 6.1 gives the following.

### Theorem 7.1 (fixed-profile overlap-one packet completion)

For every \(r,s\) and every fixed feasible slot-size profile in the
audited overlap-one zero-winding construction, the entire packet admits
pairwise vertex-disjoint full ambient wreath completions. In particular,

\[
 \boxed{\text{its integral full-vertex congestion is }1.}
 \tag{7.4}
\]

The exact packet size is

\[
 \prod_j[z^{\alpha_j}]C_{\min(j,s-j)}(z)
 \prod_h[z^{\beta_h}]C_{\min(h,s-1-h)}(z)
 \le\operatorname{Cat}_q,
 \tag{7.5}
\]

where \(\alpha_j,\beta_h\) are the fixed block semilengths. The inequality
also follows injectively by concatenating the Dyck blocks in (7.3).

This is the promised genuine use of PBBS chronology. It compiles the
entire content fibre, not merely one sector. Different size profiles use
different core-coordinate permutations, so (7.4) does not synchronize
different profiles.

The overlap-one family lies inside the already-counted zero-endpoint-excess
sector. Thus Theorem 7.1 is a new integral completion statement, not a new
global cardinality bound for that sector. Its relevance is that it proves
the adaptive mechanism exactly and supplies the genuine counterexample to
uniform completion in Section 8.

## 8. Genuine PBBS obstruction to uniform core orders

This section shows that the uniform reciprocal-binomial pointwise estimate
is false even inside the audited overlap-one family. The adaptive theorem
above remains valid for the same packet.

Fix \(\alpha>0\). For all sufficiently large \(r\), choose an odd integer
\(s\) satisfying

\[
 \frac{\alpha\sqrt r}{3}\le s\le\frac{\alpha\sqrt r}{2},
 \qquad q=r-s,
 \qquad j_0=\frac{s-1}{2},
 \qquad t=j_0.
 \tag{8.1}
\]

Then \(s+1\le\lceil\alpha\sqrt r\rceil\). In (7.1), take every block
empty except \(S_{j_0}=C\), and give \(C\) semilength \(q\) and height at
most \(t\). By the audited overlap-one theorem, every such choice is an
actual first simple zero-winding PBBS return of gap \(2s+1\). Explicitly,

\[
 D_0(C)=1^s0^{s-j_0}C0^{j_0}.
 \tag{8.1a}
\]

The active omitted labels are independent of the contents of \(C\):

\[
 a_h=
 \begin{cases}
  u-h,&h\le j_0,\\
  u-(h+2q),&h>j_0,
 \end{cases}
 \qquad
 b_h=u+s-h.
 \tag{8.1b}
\]

The \(2s+1\) half-open labels are distinct because \(s<r\). Thus all
these roots have one common active packet, and their residual cores
\(K_C,K'_C\) are respectively the 1- and 0-positions of \(C\).

Put

\[
 D=\lfloor t/4\rfloor
\]

and let the residual target word be

\[
 M=1^{2D}(10)^{q-2D}0^{2D}.
 \tag{8.2}
\]

It is Dyck of semilength \(q\) and height \(2D+1\le t\). Let

\[
 T=U\cup\{\hbox{the 1-positions of }M\}.
 \tag{8.3}
\]

For \(1\le d\le\lfloor D/4\rfloor\), choose \(d\) of the \(q-2D\)
up-steps and \(d\) of the \(q-2D\) down-steps in the central alternating
block of (8.2), and interchange their bits. Every resulting word \(K\)
is balanced and has Johnson distance \(d\) from \(M\). During the central
block its height differs from that of \(M\) by at most \(2d\). Therefore

\[
 2D-2d>0,
 \qquad
 2D+1+2d\le t
\]

for all sufficiently large \(r\). Thus every such \(K\) is a permitted
height-\(t\) Dyck core, and there are exactly

\[
 \binom{q-2D}{d}^2
 \tag{8.4}
\]

of them.

The target (8.3) has active trace \(U\). For a core at distance \(d\),
the odd-tail index is \(q-d\), so its uniform tail probability is

\[
 \binom qd^{-2}.
\]

Consequently the uniform tail load satisfies

\[
 \Lambda_T^{\rm unif}
 \ge
 \sum_{d=1}^{\lfloor D/4\rfloor}
 \left(\frac{\binom{q-2D}{d}}{\binom qd}\right)^2.
 \tag{8.5}
\]

For \(d\le D/4\),

\[
 \frac{\binom{q-2D}{d}}{\binom qd}
 =\prod_{a=0}^{d-1}\left(1-\frac{2D}{q-a}\right).
\]

Since \(D=O_\alpha(\sqrt q)\), for large \(r\) every factor has argument
at most \(1/2\), and \(\log(1-x)\ge-2x\) gives

\[
 \frac{\binom{q-2D}{d}}{\binom qd}
 \ge\exp\!\left(-\frac{4Dd}{q-d+1}\right)
 \ge\exp\!\left(-\frac{D^2}{q-d+1}\right).
 \tag{8.6}
\]

For all sufficiently large \(r\),

\[
 \left\lfloor\frac D4\right\rfloor
 \ge\frac{s}{64}\ge\frac{\alpha\sqrt r}{192},
 \qquad
 \frac{2D^2}{q-D/4}\le\frac{\alpha^2}{64}.
\]

Equations (8.5)--(8.6) therefore give the explicit bound

\[
 \boxed{
  \Lambda_T^{\rm unif}
  \ge \frac{\alpha}{192}e^{-\alpha^2/64}\sqrt r.
 }
 \tag{8.7}
\]

It remains to check the insertion/removal collar; distinct open vertices
alone do not imply projected-edge disjointness. For every selected swap
word \(C\), its initial 1-run \(\rho(C)\) satisfies

\[
 \rho(C)\le2D+2d+1<j_0.
 \tag{8.8}
\]

The exact normalized trajectory is

\[
 D_h(C)=1^s0^{s-j_0+h}C0^{j_0-h},
 \qquad 0\le h\le j_0,
 \tag{8.9}
\]

and

\[
 D_h(C)=1^{h-j_0-1}C1^{s-h+j_0+1}0^s,
 \qquad j_0+1\le h\le s+1.
 \tag{8.10}
\]

If \(1\le h\le j_0\), then after the common prefix
\(1^s0^{s-j_0}\), the word \(D_h(C)\) has an extra zero whereas every
\(D_0(C')\) has the first symbol of the Dyck word \(C'\), namely one.
Thus \(D_h(C)\ne D_0(C')\). If \(j_0<h\le s+1\), (8.8) makes the
initial 1-run of \(D_h(C)\) strictly shorter than \(s\), whereas
\(D_0(C')\) begins with \(1^s\). Hence

\[
 D_h(C)\ne D_0(C')
 \qquad(1\le h\le s+1).
 \tag{8.11}
\]

Every selected residence support is the same translated block of \(s+2\)
consecutive directed step-two edges and is nonwrapping. If two supports
overlapped, identifying a common directed edge by either endpoint would
give an equality in (8.11), after exchanging \(C,C'\) if necessary. The
case \(C=C'\) also rules out a shorter wrap. Thus the selected swap-ball
sectors are pairwise projected-edge-disjoint.

This collar restriction is essential. The entire height-capped
fixed-profile packet can contain a boundary conflict, so projected-edge
disjointness is asserted only for the explicit swap ball above.

We have therefore proved:

### Theorem 8.1 (uniform completion is false on genuine PBBS packets)

For every fixed \(\alpha>0\), there are projected-edge-disjoint families
of genuine simple PBBS returns of residence at most
\(\lceil\alpha\sqrt r\rceil\) and middle targets \(T\) for which the
uniform reciprocal-binomial tail load is \(\Omega_\alpha(\sqrt r)\).
The same families admit integral full ambient completions of congestion one
by Theorem 7.1.

Thus uniform completion and adaptive completion have genuinely different
truth values already inside one chronology-native packet.

In particular, the formerly proposed assertion

\[
 \sup_T\sum_{I\in\mathcal P}\pi_I(T)=O_\alpha(1)
\]

for every projected-edge-disjoint Gaussian PBBS family is false. Its
double-counting implication remains correct, but it is not an available
sufficient theorem. The replacement target is the adaptive dual (3.4).

## 9. Exact linear uniform load on the full Dyck sentinel matching

There is a sharper local calculation which explains Theorem 8.1. Order a
\(2q\)-set as \([2q]\), and let \(\mathcal D_q\) be all Dyck \(q\)-subsets.
For the mountain

\[
 S=\{1,\ldots,q\},
\]

the number of \(K\in\mathcal D_q\) at Johnson distance \(j\) from \(S\)
is

\[
 \left[\binom qj-\binom q{j-1}\right]^2.
 \tag{9.1}
\]

Indeed, the first \(q\) steps contain \(j\) down-steps and must be a ballot
path; reflection gives \(\binom qj-\binom q{j-1}\) choices. Reversing and
complementing the suffix gives the same independent count.

The \(j=0\) target is the fixed open endpoint and is excluded from the
tail. Dividing (9.1) by the odd kernel denominator \(\binom qj^2\) gives

\[
 \begin{aligned}
 \Lambda_S^{\rm unif}
 &=\sum_{j=1}^{\lfloor q/2\rfloor}
   \left(\frac{q-2j+1}{q-j+1}\right)^2\\
 &=q\int_0^{1/2}\left(\frac{1-2x}{1-x}\right)^2dx+O(1)\\
 &=\boxed{(3-4\log2)q+O(1)}.
 \end{aligned}
 \tag{9.2}
\]

On the other hand, the Dyck sets are precisely the sentinel edges of the
MSW factor, so Theorem 6.1 gives an integral congestion-one completion.
This full Dyck packet is a factor-compatible open-sector packet; it is not
needed to assert that every one of its sectors is an actual PBBS return.
The genuine statement is Theorem 8.1.

## 10. Exact fixed-core obstruction to all generic Hall proofs

Fix one active pair \((A,U)\) and a \(2q\)-set \(R\). Take one abstract
simple open-wreath sector for every unordered bipartition

\[
 R=K\mathbin{\dot\cup}K',\qquad |K|=|K'|=q.
\]

Choose either orientation for each unordered pair. The weighted
calculations below do not depend on that choice: under
\(K\leftrightarrow K'\), the even index changes
\(j\leftrightarrow q-1-j\), and

\[
 \binom qj\binom q{j+1}
 =
 \binom q{q-1-j}\binom q{q-j};
\]

the odd index changes \(j\leftrightarrow q-j\), and
\(\binom qj=\binom q{q-j}\).

Their open Kneser paths are pairwise vertex-disjoint, hence edge-disjoint
on those displayed paths: restriction of an open state to \(R\) recovers
\(K\) or \(K'\), and each unordered pair is used once. No canonical PBBS
insertion/removal collar is asserted for this abstract family.

Fix \(T=A\cup S\), where \(|S|=q-1\). For ordered partitions with

\[
 j=|S\cap K'|,
\]

the number is

\[
 \binom{q-1}j\binom{q+1}{j+1}.
\]

After multiplication by the even kernel

\[
 \frac1{\binom qj\binom q{j+1}},
\]

every \(j\) contributes exactly \((q+1)/q\). Dividing by two for
unordered partitions and summing \(j=0,\ldots,q-1\) gives

\[
 \boxed{\Lambda_T^{\rm unif}=\frac{q+1}{2}.}
 \tag{10.1}
\]

Similarly, for \(T=U\cup S\), \(|S|=q\), every internal odd index
contributes one before division by two, so

\[
 \boxed{\Lambda_T^{\rm unif}=\frac{q-1}{2}.}
 \tag{10.2}
\]

The number of sectors is

\[
 M=\frac12\binom{2q}q.
\]

Every tail has \(2q-1\) vertices, and all tails lie in the common support

\[
 \Omega(A,U;R)
 =\{A\cup Y:Y\in\tbinom R{q-1}\}
  \mathbin{\dot\cup}
  \{U\cup X:X\in\tbinom Rq\},
\]

whose size is

\[
 \binom{2q}{q-1}+\binom{2q}q
 =\frac{2q+1}{q+1}\binom{2q}q.
\]

Therefore every fractional or integral adaptive completion has maximum
tail load at least

\[
 \boxed{
  \frac{M(2q-1)}{|\Omega(A,U;R)|}
  =\frac{(q+1)(2q-1)}{2(2q+1)}
  \sim\frac q2.}
 \tag{10.3}
\]

This is not a canonical PBBS family. It proves exactly that fixed-core
normal form, two endpoint-owner nonreuse, local factorial completions, and
open-path edge disjointness cannot establish bounded adaptive congestion.
The simultaneous PBBS cyclic-ballot constraints are indispensable.

### 10.1 The exact two-endpoint corridor

There is a stronger necessary condition which genuinely uses both endpoint
stars. Put

\[
 V=A\setminus\{a_0\}=\{a_1,\ldots,a_s\}.
\]

Order the other \(2r\) ambient coordinates cyclically after the returned
coordinate \(a_0\). For every prefix \(P\) of this order, define

\[
 g(P)=|P\cap U|-|P\cap V|,
 \qquad
 c_K(P)=|P\cap K|-|P\cap K'|.
 \tag{10.4}
\]

### Lemma 10.1 (two-owner PBBS corridor)

Every genuine simple PBBS return satisfies

\[
 \boxed{g(P)\ge |c_K(P)|\qquad\text{for every prefix }P.}
 \tag{10.5}
\]

Consequently the \(U/V\) incidence word obtained after deleting all core
coordinates is a Dyck word.

#### Proof

The two endpoint states are \(K\cup U\) and \(K'\cup U\), and both
endpoint edges omit \(a_0\). Their canonical incidence words, read after
\(a_0\), are Dyck. At prefix \(P\), their heights are respectively

\[
 g(P)+c_K(P),\qquad g(P)-c_K(P).
 \tag{10.6}
\]

Both quantities are nonnegative, which is exactly (10.5). Both have full
sum zero. Deleting the horizontal core steps from \(g\) therefore leaves
a nonnegative balanced \(U/V\) walk. \(\square\)

This is the exact information supplied jointly by the rank-\((r+1)\)
owners \(A\cup K\) and \(A\cup K'\). It is stronger than two unrelated
endpoint-degree bounds. Conversely, for fixed \(A,U,K,K'\) and ambient
coordinate order, (10.5) is equivalent to the two endpoint incidence words
being Dyck; no endpoint information was lost in passing to the corridor.

### 10.2 Even the exact endpoint corridor is insufficient

The next construction is an endpoint-level obstruction, not a PBBS
counterexample. It shows that the intermediate same-row chronology cannot
be discarded.

Fix \(q\ge9\), and put

\[
 s=\lceil2\sqrt q\rceil,\qquad r=q+s,
 \qquad N=2r+1.
 \tag{10.7}
\]

After a distinguished coordinate \(a_0\), arrange the other coordinates
in three consecutive ambient blocks

\[
 U,\quad R,\quad V,
 \qquad |U|=|V|=s,\quad |R|=2q,
 \tag{10.8}
\]

and set \(A=\{a_0\}\mathbin{\dot\cup}V\). Let
\(\mathcal B_{q,s}\) be the balanced binary words \(c\) on \(R\) whose
signed prefix height \(C_t\) satisfies

\[
 |C_t|\le s\qquad(0\le t\le2q).
 \tag{10.9}
\]

For each complement orbit \(\{c,\bar c\}\), take one formal fixed-active
open sector with unordered core pair \(\{K,K'\}\), where \(K\) is the
one-set of \(c\). Complementation has no fixed binary word, so each orbit
has size two.

Put \(a=s+1\). Reflection after the first visit to height \(+a\) gives
exactly \(\binom{2q}{q+a}\) balanced bridges which visit \(+a\); the
same count holds for \(-a\). Hence

\[
 |\mathcal B_{q,s}|
 \ge \binom{2q}q-2\binom{2q}{q+a}.
 \tag{10.10}
\]

Moreover,

\[
 \begin{aligned}
 \frac{\binom{2q}{q+a}}{\binom{2q}q}
 &=\prod_{i=1}^{a}\frac{q-i+1}{q+i}\\
 &\le \exp\!\left(-\frac{a^2}{q+a}\right)
 \le e^{-2}.
 \end{aligned}
 \tag{10.11}
\]

Indeed \(a\le q\) for \(q\ge9\), and
\(a^2\ge4q\), while \(q+a\le2q\). Thus the number \(M\) of unordered
sectors obeys

\[
 M\ge\frac{1-2e^{-2}}2\binom{2q}q.
 \tag{10.12}
\]

Every selected sector passes both genuine endpoint-star tests: its two
normalized endpoint words are

\[
 1^s c0^s,\qquad 1^s\bar c0^s,
 \tag{10.13}
\]

which are Dyck by (10.9). Equivalently, the exact corridor (10.5) holds.
Distinct unordered core pairs have disjoint displayed open vertex sets,
because restriction of any open state to \(R\) recovers \(K\) or \(K'\).
Thus their displayed open edges are pairwise disjoint, and every endpoint
owner of either form \(A\cup K\) or \(A\cup K'\) has multiplicity one.
No projected PBBS collar outside these displayed formal paths is asserted.

Nevertheless all completion tails lie in the common support

\[
 \Omega=
 \{A\cup Y:Y\in\tbinom R{q-1}\}
 \mathbin{\dot\cup}
 \{U\cup X:X\in\tbinom Rq\},
 \tag{10.14}
\]

whose size is

\[
 |\Omega|=\binom{2q}{q-1}+\binom{2q}q
 =\frac{2q+1}{q+1}\binom{2q}q.
 \tag{10.15}
\]

Every sector contributes exactly \(2q-1\) units of tail mass under every
fractional adaptive assignment. Averaging over (10.14), (10.12) gives

\[
 \boxed{
 C^*\ge(1-2e^{-2})
 \frac{(q+1)(2q-1)}{2(2q+1)}=\Omega(q).}
 \tag{10.16}
\]

This lies in a fixed Gaussian window, since

\[
 s+1\le2\sqrt q+2\le3\sqrt r\qquad(q\ge9).
 \tag{10.17}
\]

The construction satisfies fixed-active geometry, disjoint formal open
traces, endpoint-owner nonreuse, and both canonical endpoint-star Dyck
conditions. It does **not** assert the intermediate states are successive
states of one canonical PBBS trajectory. Thus (10.16) proves exactly that
the pair of endpoint owners, even with its sharp corridor, is not enough;
the omitted input is the simultaneous intermediate chronology (12.1).

### 10.3 Exact cost of covering the unrestricted family by sentinel packets

Let \(\mathcal E_q\) be all unordered complementary \(q\)-set pairs in
one fixed \(2q\)-set. Then

\[
 |\mathcal E_q|=\frac12\binom{2q}q
 =\frac{q+1}{2}\operatorname{Cat}_q.
 \tag{10.18}
\]

Define \(\theta^*_{\rm sent}(\mathcal E_q)\) to be the minimum
\(\sum_Mw_M\) over nonnegative weights on subpackets \(M\) of sentinel
matchings of exact core factors, subject to
\(\sum_{M\ni e}w_M\ge1\) for every \(e\in\mathcal E_q\).
Its finite LP dual is

\[
 \theta^*_{\rm sent}(\mathcal E_q)
 =\max\left\{
   \sum_{e\in\mathcal E_q}z_e:
   z_e\ge0,\ 
   \sum_{e\in M}z_e\le1\text{ for every sentinel packet }M
 \right\}.
 \tag{10.18a}
\]

Fix one exact MSW factor on \(R\cup\{\infty\}\). Its sentinel matching
has exactly \(\operatorname{Cat}_q\) edges, one per core wreath row. Let
\(M_\sigma\) be this matching after relabelling \(R\) by
\(\sigma\in S_{2q}\), retaining the permutations as an indexed family
even when two indices give the same matching. The symmetric group is transitive on
\(\mathcal E_q\), so every edge belongs to the same number \(d\) of the
packets \(M_\sigma\). Double counting gives

\[
 (2q)!\operatorname{Cat}_q=d|\mathcal E_q|.
 \tag{10.19}
\]

Giving every \(M_\sigma\) weight \(1/d\) is a fractional packet cover of
total weight

\[
 \frac{(2q)!}{d}
 =\frac{|\mathcal E_q|}{\operatorname{Cat}_q}
 =\frac{q+1}{2}.
 \tag{10.20}
\]

Conversely, every sentinel matching contains at most
\(\operatorname{Cat}_q\) pairs. Summing the cover inequalities over all
members of \(\mathcal E_q\) proves the reverse inequality. Equivalently,
the constant dual weight \(z_e=1/\operatorname{Cat}_q\) is feasible in
(10.18a) and has value \((q+1)/2\). Therefore

\[
 \boxed{\theta^*_{\rm sent}(\mathcal E_q)=\frac{q+1}{2}.}
 \tag{10.21}
\]

There is no orientation factor: a sentinel edge is unordered, and its row
can be reversed. Lemma 6.2 supplies adaptive congestion at most
\((q+1)/2\), whereas (10.3) supplies the universal lower bound

\[
 \frac{(q+1)(2q-1)}{2(2q+1)}
 =\frac{2q-1}{2q+1}\theta^*_{\rm sent}(\mathcal E_q).
 \tag{10.22}
\]

Thus the weighted sentinel-packet upper bound is asymptotically sharp on
the unrestricted complementary family: its ratio to the universal
adaptive tail-congestion lower bound is \((2q+1)/(2q-1)\). This does not
assert equality for optimal adaptive congestion. In particular, the
packet reduction cannot by itself produce a bounded cover. PBBS chronology
must force a much smaller packet-cover number or permit adaptive
completions not representable by such packets.

## 11. A common-priority chronology graph

There is one further exact reduction of the uniform load which may be
useful for the remaining cross-packet problem. Give every coordinate one
independent continuous priority and restrict that order to every core.
For a fixed target \(T\), let \(E_I(T)\) be the event that sector \(I\)'s
priority completion contains \(T\). Then

\[
 \Pr E_I(T)=\pi_I(T).
\]

For an odd-tail sector the event is

\[
 T\cap K_I\prec K_I\setminus T,
 \qquad
 K'_I\setminus T\prec T\cap K'_I,
 \tag{11.1}
\]

while for an even-tail sector both inequalities reverse. Here
\(C\prec D\) means every priority in \(C\) precedes every priority in
\(D\).

Thus two equal-sign events are disjoint if either

\[
 K_I\cap K'_J\quad\hbox{or}\quad K'_I\cap K_J
\]

is bichromatic across \((T,T^c)\). Two opposite-sign events are disjoint
if either

\[
 K_I\cap K_J\quad\hbox{or}\quad K'_I\cap K'_J
\]

is bichromatic. A bichromatic pair would otherwise force both
\(x\prec y\) and \(y\prec x\).

Let \(G_T\) be the graph joining such mutually exclusive events. Every
clique has total event probability at most one. Therefore

\[
 \boxed{
  \sum_I\pi_I(T)\le\operatorname{cc}_f(G_T),}
 \tag{11.2}
\]

where \(\operatorname{cc}_f\) is the fractional clique-cover number. The
counterexample in Section 8 shows that \(\operatorname{cc}_f(G_T)\) need
not be bounded on genuine packets for the uniform measure; an adaptive
argument must use the MSW-type correlated choices instead.

## 12. Exact remaining theorem and audited boundary

For a fixed active word and core \(K\subseteq R\), the formal states
(1.1)--(1.2) form an actual canonical PBBS segment exactly when, for every
time \(t=0,\ldots,2s+1\), the cyclic word beginning at the omitted label
\(\lambda_t\) is \(0D_t\) with \(D_t\) Dyck. Equivalently, for every
\(1\le\ell\le2r\),

\[
 \sum_{p=1}^{\ell}
 \left(2\mathbf1_{\{\lambda_t+p\in X_t(K)\}}-1\right)\ge0,
 \tag{12.1}
\]

with cyclic indices; the full sum is zero. This simultaneous cyclic-ballot
system is the precise chronology missing from Section 10.

Its two endpoint instances imply the corridor (10.5), but Section 10.2
shows that those endpoint instances alone still permit linear adaptive
congestion. Any successful argument must compare the intermediate ballot
conditions for the same row; separate endpoint tests cannot suffice.

The report proves that one large, nontrivial solution fibre of (12.1) --
the fixed-profile overlap-one zero-winding fibre -- contracts to one exact
core factor and hence has congestion one. It also proves that uniform
orders can have \(\Omega_\alpha(\sqrt r)\) load on that same fibre.

The unresolved global statement can now be written without ambiguity.

> **Fractional cross-packet adaptive completion theorem -- UNPROVED.**
> For every fixed \(\alpha>0\), every projected-edge-disjoint family of
> genuine simple PBBS returns with
> \(s+1\le\lceil\alpha\sqrt r\rceil\) admits distributions on the path
> sets (2.2) whose total tail congestion is \(O_\alpha(1)\).

By Theorem 3.1, this fractional statement is equivalent to the weighted
min-cost-path cuts

\[
 \sum_I d_I(y)\le C_\alpha\sum_Ty_T
 \qquad(y\ge0),
 \tag{12.2}
\]

and its constant cut already implies the Catalan packing bound. The
stronger integral alternative asks for one path from each \(\Omega_I\)
with bounded target capacity. It implies the fractional theorem, but no
converse rounding theorem is proved here.

Lemma 6.2 gives a concrete sufficient strengthening: it is enough to cover
every genuine sector fractionally by core-factor-compatible sentinel
packets with total weight \(O_\alpha(1)\). Equation (10.21) proves that this
strengthening is false for the unrestricted complementary-core family with
the sharp cost \((q+1)/2\). It remains viable only if simultaneous PBBS
chronology forces a bounded cover, or if one uses adaptive distributions
which do not decompose into congestion-one sentinel packets.

Theorems
5.1 and 7.1 prove respectively:

\[
 \begin{array}{c}
 \text{bounded composed load at each of }O(\sqrt r)
 \text{ endpoint layers},\\[1mm]
 \text{and congestion one inside every fixed-profile overlap-one packet.}
 \end{array}
\]

What remains is exactly to stop target capacity from being recycled across
different recursion times, slot-size profiles, and positive-winding
packets, using the intermediate constraints for one actual row. No
uniform-kernel or endpoint-only assertion remains available.

## 13. Audit notes

1. Every completion choice in Sections 2--7 is one path in one exact DAG;
   no separate per-layer choices are composed after the fact.

2. The fractional prefix bound (5.6) does not imply constant total
   congestion: its sum over \(\Theta(\sqrt r)\) layers is only
   \(O_\alpha(\sqrt r)\).

3. The integral one-step Hall bound (5.3) accumulates ceilings. No
   constant integral prefix bound is claimed from that recurrence.

4. The MSW packet theorem uses one common core-coordinate order only
   after the slot-size profile is fixed. It is not applied across
   different profiles.

5. The generic packet in Section 10 is not claimed to satisfy PBBS
   chronology. The family in Section 8 does satisfy the audited
   overlap-one chronology and is used only to refute uniform completions,
   not adaptive ones.

6. No consequence from any false return converse is used anywhere in this
   report.

7. The sentinel contraction and every tail/open collision case in
   Theorem 7.1 were independently audited. The first draft of Section 8
   incorrectly inferred projected-edge disjointness from open-state
   disjointness; an independent audit found the possible removal-edge
   collar collision. Equations (8.8)--(8.13) are the corrected complete
   directed-edge check.

8. Lemma 6.2 normalizes separately for each sector by its exact cover mass
   \(c_I\); it does not pretend that independently sampled sectors are
   jointly disjoint. Only the expected fractional load is bounded.

9. Section 10.2 asserts genuine PBBS validity only for the two endpoint
   star edges. Its intermediate open path is a formal fixed-core path, not
   an asserted canonical PBBS return. Accordingly (10.16) is a no-go for
   endpoint-only arguments, not a counterexample to the remaining theorem.

10. The reflection count uses complement orbits of size exactly two, and
    the sentinel cover uses unordered complementary edges. Both factors
    of two in (10.12) and (10.18) are therefore retained; row reversal
    introduces no further orientation factor.

11. Lemma 6.2 and Sections 10.1--10.3 were independently audited after
    insertion. The probability normalization, reflection constant,
    Gaussian-window inequality, unordered orientation factors, and
    full-versus-tail congestion scopes all passed.
