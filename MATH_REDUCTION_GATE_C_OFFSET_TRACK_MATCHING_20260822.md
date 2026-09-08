# Gate C: offset-track reduction, balanced flag flow, and the remaining colored matching

**Status (2026-08-22).**  This note proves four facts.

1. Every target in the middle band produced by a FIFO atom is an
   intersection or union of two nearby middle windows.  Thus a fragment uses
   one structured track of middle windows, not \(L(2H+1)\) unrelated tokens.
2. Ignoring FIFO adjacency, one nested flag through every middle set can
   always be chosen with optimally balanced load at every controlled rank.
3. Independent choices of those balanced flag columns almost never serialize.
   Moreover, small codegree and small summed squared influence do not by
   themselves imply a large matching.
4. A quantitatively near-perfect matching of **extended middle tracks**, with
   small aggregate offset-color overflow, would compile to a coefficient-one
   word.

The last matching statement is not proved here.  It is the exact surviving
Gate-C condition.  In particular, the bounds \(H/b+LH/b^2=o(1)\) below are
valid for independent abstract flags but are not a quenched FIFO influence
bound.

## 1. The word problem and the phase-refined atoms

Let \(\Omega\) have size \(2b\), where

\[
 b=2h+1\ge5,\qquad {\cal V}={\Omega\choose b},\qquad
 W=|{\cal V}|={2b\choose b}.                                      \tag{1.1}
\]

A word is a finite sequence of subsets of \(\Omega\).  It realizes \(T\ne
\varnothing\) when \(T\) is the union of a nonempty consecutive interval of
letters.  Let \(\nu(2b)\) be the minimum length of a word realizing every
nonempty subset of \(\Omega\).

Split \(\Omega=A\mathbin{\dot\cup}B\), with both shores of size \(b\), choose
a directed cyclic order on each shore, and repeat the type period

\[
 B,A,B,A,\ldots,B,A,B.                                           \tag{1.2}
\]

At successive events of one type emit successive elements of its cyclic
order.  Stream roots lie in \(\mathbb Z_b^2\).  Advancing by one whole type
period changes them by \((h,h+1)\), which has order \(b\).  Retain one phase
label in

\[
 Q=\mathbb Z_b^2/\langle(h,h+1)\rangle.                           \tag{1.3}
\]

A phase-refined atom is the resulting cyclic word
\((w_t)_{t\in\mathbb Z_{b^2}}\), together with all these labels.  Put

\[
 C_t=\{w_t,w_{t+1},\ldots,w_{t+b-1}\}.                            \tag{1.4}
\]

There are

\[
 \widehat N=bW((b-1)!)^2                                         \tag{1.5}
\]

labelled atoms.  Every atom contains \(b^2\) distinct middle sets, and the
labelled family is invariant under every permutation of \(\Omega\).
Consequently every middle set has atom degree

\[
 \widehat D={\widehat N b^2\over W}=b(b!)^2.                      \tag{1.6}
\]

For completeness, the chronology facts used below follow directly from
(1.2).  Every length-\(b\) type window has \(h\) \(A\)-events and \(h+1\)
\(B\)-events.  Its two shore parts are cyclic intervals.  At a fixed time
residue, advancing a period moves their starts by \((h,-h)\); since
\(\gcd(h,b)=1\), all \(b\) pairs on the corresponding diagonal occur.  The
\(b\) time residues give all of \(\mathbb Z_b^2\), proving that the \(C_t\)
are distinct.  A coordinate recurs after \(b\) events of its own type.
The \(B\)-event gaps are \(2,\ldots,2,1\), and the \(A\)-event gaps are
\(2,\ldots,2,3\).  Hence every recurrence gap is at least \(2b-2\), so every
block of at most \(2b-2\) consecutive emissions is injective.

The exact normalized pair profile, which will only be used through its
maximum, is

\[
 {\widehat\lambda_d\over\widehat D}
 ={4\min(d,b-d)\over {b\choose d}^2},\quad 1\le d<b,
 \qquad \widehat\lambda_b=0,                                   \tag{1.7}
\]

where \(d=|S-T|\) is Johnson distance.  To prove it, relative to one cyclic
interval on a \(b=2h+1\) cycle there are two intervals at each distance
\(1,\ldots,h\).  Convolving the two shore profiles gives
\(4\min(d,b-d)\) cells at distance \(d\).  Double counting atom--cell
pairs gives (1.7).  In particular

\[
 \max_{S\ne T}{\operatorname{codeg}(S,T)\over\widehat D}
 ={4\over b^2}.                                                   \tag{1.8}
\]

## 2. Offset colors are functions of nearby middle windows

Assume \(1\le q\le H\le b-2\).  Define the lower and upper colors at start
\(t\) by

\[
 T^-_q(t)=\{w_t,\ldots,w_{t+b-q-1}\},\qquad
 T^+_q(t)=\{w_t,\ldots,w_{t+b+q-1}\}.                            \tag{2.1}
\]

### Theorem 2.1 (offset-pair identity)

For every atom and every \(t\),

\[
 \boxed{T^-_q(t)=C_{t-q}\cap C_t,\qquad
        T^+_q(t)=C_t\cup C_{t+q},\qquad
        d_J(C_t,C_{t+q})=q.}                                    \tag{2.2}
\]

#### Proof

The union of the positional intervals defining \(C_{t-q}\) and \(C_t\)
has \(b+q\le2b-2\) emissions and is injective.  Their set intersection is
therefore exactly their positional overlap, namely the first set in (2.1).
The same argument for \(C_t,C_{t+q}\) makes their union the second set in
(2.1).  Exactly \(q\) elements leave and \(q\) enter, proving the distance
identity. \(\square\)

Thus all band tokens with core starts \(a,\ldots,a+L-1\) are determined by
the single extended track

\[
 C_{a-H},C_{a-H+1},\ldots,C_{a+L+H-1}.                           \tag{2.3}
\]

This is the promised structured replacement for a generic
\(L(2H+1)\)-resource edge.

## 3. The annealed flag-overlap calculation

A band flag through \(C\in{\cal V}\) is a nested sequence

\[
 S_{b-H}\subset\cdots\subset S_b=C\subset\cdots\subset S_{b+H}.
                                                                    \tag{3.1}
\]

Choose it uniformly by independently ordering the elements deleted from
\(C\) and the elements added from \(\Omega-C\).  If \(C,C'\) have Johnson
distance \(d\), two independent flags through them have the same lower
depth-\(q\) target, or the same upper depth-\(q\) target, with probability

\[
 p_{q,d}=
 \begin{cases}
 \displaystyle{{b-d\choose q-d}\over {b\choose q}^2},&d\le q,\\[6pt]
 0,&d>q.
 \end{cases}                                                     \tag{3.2}
\]

Indeed, a common lower target is a \((b-q)\)-subset of \(C\cap C'\);
a common upper target is a \((b+q)\)-superset of \(C\cup C'\).  Both counts
are \({b-d\choose q-d}\), while each marginal has \({b\choose q}\) choices.

For \(1\le q\le(b-1)/2\),

\[
 p_{q,0}={1\over {b\choose q}}\le {1\over b},\qquad
 \max_{d\ge1}p_{q,d}=p_{q,1}\le {1\over b^2}.                     \tag{3.3}
\]

The numerator in (3.2) decreases with \(d\).  At \(d=1\),
\(p_{q,1}=(q/b)/{b\choose q}\); and
\({b\choose q}\ge bq\), by equality for \(q=1\) and by
\({b\choose q}\ge {b\choose2}\ge bq\) otherwise.

Summing both shores through depth \(H\), one same-column comparison costs at
most \(2H/b\), while each different-column comparison costs at most
\(2H/b^2\).  Hence one same column and \(L-1\) distinct other columns have
total annealed influence

\[
 O\!\left({H\over b}+{LH\over b^2}\right).                        \tag{3.4}
\]

This does not survive conditioning on an exposed FIFO track.  The identities

\[
 T^-_1(t+1)=C_t\cap C_{t+1},\qquad
 T^+_1(t)=C_t\cup C_{t+1}                                       \tag{3.5}
\]

show that after neighboring middle windows are known, the corresponding
collision event can have conditional probability one.  Therefore (3.4)
cannot be inserted as a quenched dependency bound in a nibble or local lemma
without an additional product-specific exposure theorem.

## 4. Exact integral balancing of abstract flag columns

### Theorem 4.1 (balanced nested-flag bank)

For every \(H\le b\), one can choose one band flag (3.1) through every
\(C\in{\cal V}\) so that, simultaneously for every
\(s\in\{b-H,\ldots,b+H\}\), every \(s\)-set occurs in

\[
 \left\{\left\lfloor{W\over {2b\choose s}}\right\rfloor,
             \left\lceil{W\over {2b\choose s}}\right\rceil\right\}
                                                                    \tag{4.1}
\]

chosen flags.

#### Proof

We prove the lower half; reverse inclusions for the upper half.  Form the
layered containment digraph from rank \(b\) down to rank \(b-H\).  Give every
rank-\(s\) vertex a throughput interval

\[
 \left[\lfloor\mu_s\rfloor,\lceil\mu_s\rceil\right],
 \qquad \mu_s={W\over {2b\choose s}},                              \tag{4.2}
\]

and feed one unit into every rank-\(b\) vertex.  A feasible fractional flow
sends the \(\mu_s\) units at an \(s\)-set equally over its \(s\) immediate
subsets.  An \((s-1)\)-set then receives

\[
 {2b-s+1\over s}\mu_s=\mu_{s-1}.                                  \tag{4.3}
\]

Split each vertex into an in-node and an out-node, putting (4.2) on the
joining arc.  This is an ordinary network with integer lower and upper
capacities and an integer supply vector.  Its feasible-flow polytope has an
integral point: after subtracting lower bounds, feasibility is a standard
circulation problem, and the directed incidence matrix is totally
unimodular.  A self-contained determinant proof is as follows.  In every
square submatrix of an incidence matrix, a column with at most one nonzero
permits induction by expansion; if every column has two nonzeros, the row
sum is zero and the determinant vanishes.  Thus every subdeterminant is
\(0,\pm1\), and an integral basic feasible solution exists.

Decompose the integral acyclic flow into unit paths.  Since each middle
source supplies exactly one unit, this gives one lower chain through every
\(C\), with the loads (4.1).  The reversed construction gives one upper
chain through every \(C\); pair the two chains with their common middle
source. \(\square\)

Every individual flag in Theorem 4.1 embeds in some phase-refined atom when
\(H\le b-4\).  Write its lower bottom set as \(R\), list the \(H\) remaining
central elements in the order in which the lower chain adds them, and then
list the \(H\) upper additions.  This is a prescribed injective sequence of
length \(b+H\).  Assign its positions to shores according to a translate of
the type word (1.2).  In any \(b+H\le2b-4\) consecutive type positions
neither type occurs more than \(b\) times.  Assign the unused coordinates to
the two shores to fill both to size \(b\), extend the encountered same-type
orders to cyclic orders, and choose the required root-pair coset.  The
resulting atom has the prescribed flag by Theorem 2.1.

This proves that neither marginal quota integrality nor individual atom
supply is an obstruction.  It does not make neighboring chosen flags
compatible.

## 5. Independent balancing cannot be serialized

For a fixed middle set, the number of band flags is

\[
 R_H=(b)_H^2, \qquad (b)_H=b(b-1)\cdots(b-H+1).                    \tag{5.1}
\]

Represent a flag by a bottom set \(R\) of size \(b-H\), an ordered central
tail \(u_1,\ldots,u_H\), and ordered future entries \(v_1,\ldots,v_H\).
Given this flag, a compatible one-step FIFO successor is determined by
choosing

\[
 z\in R,\qquad v_{H+1}\in
 \Omega-(C\cup\{v_1,\ldots,v_H\}).                                \tag{5.2}
\]

The successor has

\[
 \begin{split}
 C'&=C-z+v_1,\\
 R'&=(R-z)\cup\{u_1\},\\
 (u'_1,\ldots,u'_H)&=(u_2,\ldots,u_H,v_1),\\
 (v'_1,\ldots,v'_H)&=(v_2,\ldots,v_H,v_{H+1}).
 \end{split}                                                       \tag{5.3}
\]

There are exactly \((b-H)^2\) compatible successor flags, distributed
\(b-H\) apiece over \(b-H\) successor middle sets.

### Theorem 5.1 (independent-serialization obstruction)

Choose independently and uniformly one band flag through every middle set.
Let \(Z\) be the number of directed compatible FIFO adjacencies.  Then

\[
 {\mathbb E Z\over W}={(b-H)^2\over(b)_H^2}.                       \tag{5.4}
\]

For every \(H\ge2\), with probability \(1-o(1)\), only \(o(W)\) chosen
columns are incident with any compatible adjacency.

#### Proof

Condition on the flag through \(C\).  It has \(b-H\) possible successor
middle sets.  At each, exactly \(b-H\) of the \(R_H\) flags are compatible.
This proves (5.4) by summing over \(C\).  The number \(I\) of incident
columns is at most \(2Z\).  For \(H\ge2\),

\[
 {(b-H)^2\over(b)_H^2}\le{1\over(b-1)^2}.                         \tag{5.5}
\]

Markov's inequality, for example at threshold \(I/W=b^{-1/2}\), proves the
claim. \(\square\)

Thus “first balance one flag per column, then serialize” loses almost all
columns.  A successful construction must correlate whole tracks.

## 6. Why local matching parameters alone cannot finish the job

For an \(r\)-uniform \(D\)-regular multihypergraph define

\[
 \Xi(v)=\sum_{w\ne v}
 \left({\operatorname{codeg}(v,w)\over D}\right)^2.                \tag{6.1}
\]

### Theorem 6.1 (parameter-only obstruction)

Let \(D\ge4\) and \(r\ge64\log(2eDr)\).  There are arbitrarily large
\(r\)-partite, \(r\)-uniform, \(D\)-regular multihypergraphs such that

\[
 \Delta_2\le2,\qquad \max_v\Xi(v)\le{2(r-1)\over D},               \tag{6.2}
\]

but a maximum matching covers at most

\[
 {32\log(2eDr)\over r}                                            \tag{6.3}
\]

of the vertices.

#### Proof

Let \(L\) tend to infinity, \(M=LD\), and independently choose \(r\)
uniform equipartitions of an \(M\)-set \(X\) into \(L\) blocks of size \(D\).
For blocks from two partitions,

\[
 \Pr(|B\cap B'|\ge3)\le{{D\choose3}^2\over{M\choose3}}.
                                                                    \tag{6.4}
\]

A union bound over \({r\choose2}L^2\) pairs shows that all cross
intersections are at most two with probability \(1-o(1)\).

Put \(Q=\log(2eDr)\), \(c=16Q/r\), and \(s=\lceil cL\rceil\).
For a fixed \(s\)-set, the probability of meeting every block of one
partition at most once is

\[
 p_s={(L)_sD^s\over(LD)_s}
 \le\exp\!\left(-{s(s-1)\over4L}\right),                         \tag{6.5}
\]

where \(c\le1/4\), \(D\ge4\), and
\(\log(1-x)\le-x,\ -\log(1-y)\le2y\) were used.  Independence and
\({M\choose s}\le(eM/s)^s\) give

\[
 {\mathbb E}Z_s\le {M\choose s}p_s^r\le e^{-sQ}=o(1).              \tag{6.6}
\]

Thus some choice of partitions has both properties and no common partial
transversal of size \(s\).

Make one hypergraph vertex for every block of every partition and, for each
\(x\in X\), one edge consisting of its \(r\) containing blocks.  It is
\(D\)-regular and (6.4) gives \(\Delta_2\le2\).  Since
\(t^2\le2t\) for \(t=0,1,2\), summing intersections against each other
partition gives \(\Xi(v)\le2(r-1)/D\).  Matchings are exactly common partial
transversals, so their covered fraction is at most
\(s/L\le32Q/r\) for large \(L\). \(\square\)

Taking \(D=r^2\) makes both \(r\Delta_2/D\) and \(\max\Xi\) tend to zero.
Replacing every edge by any common number of labelled parallel copies
inflates the absolute degree without changing normalized quantities or the
matching number.  Hence no theorem using only regularity, codegree,
(3.4)-type summed influence, and absolute degree can prove the needed
matching.  Product-specific expansion or a stronger conditional exposure
law is indispensable.

## 7. Extended-track compiler

Let

\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,\qquad
 K=L+2H,\qquad b+H\le2b-2,\qquad K\le b^2/2.                       \tag{7.1}
\]

For every labelled atom and core start \(a\), make the \(K\)-set edge

\[
 E(a)=\{C_{a-H},\ldots,C_{a+L+H-1}\}.                             \tag{7.2}
\]

This labelled extended-track hypergraph has \(W\widehat D\) edges, exact
degree

\[
 D_K=K\widehat D,                                                  \tag{7.3}
\]

and, by (1.8),

\[
 {\Delta_2\over D_K}\le {K-1\over K}{4\over b^2},
 \qquad {K\Delta_2\over D_K}\le{4K\over b^2}.                     \tag{7.4}
\]

Indeed, a target in an atom lies in exactly \(K\) cyclic tracks.  Two
distinct positions lie together in at most \(K-1\) such tracks.

Choose a matching of \(t\) extended tracks.  Retain only their \(L\) core
starts, so

\[
 M=Lt=(1-\delta)W.                                                 \tag{7.5}
\]

For \(s=b\pm q\), \(0\le q\le H\), let \(a_s(T)\) be the number of core
offset colors (2.1) equal to \(T\).  Choose balanced quotas

\[
 q_s(T)\in\{\lfloor M/N_s\rfloor,\lceil M/N_s\rceil\},\qquad
 N_s={2b\choose s},\qquad \sum_Tq_s(T)=M,                          \tag{7.6}
\]

and define one-sided overflow

\[
 V_s=\sum_T(a_s(T)-q_s(T))_+.                                     \tag{7.7}
\]

### Lemma 7.1 (holes with possibly zero quotas)

If \(h_s=|\{T:a_s(T)=0\}|\), then

\[
 h_s\le (N_s-M)_++V_s.                                            \tag{7.8}
\]

#### Proof

The load and quota vectors have equal total, so total positive excess equals
total positive deficit and is \(V_s\).  Holes at positive-quota coordinates
cost at least one unit of deficit.  If \(M<N_s\), exactly \(N_s-M\) balanced
quotas are zero; otherwise none is zero. \(\square\)

### Theorem 7.2 (conditional coefficient-one compiler)

Suppose

\[
 {b+H\over L}=o(1),\qquad
 \delta=o(b^{-1/3}),\qquad
 \sum_{s=b-H}^{b+H}V_s=o(W).                                      \tag{7.9}
\]

Then

\[
 \nu(2b)=(1+o(1)){2b\choose b}.                                  \tag{7.10}
\]

#### Proof

For each chosen track concatenate the singleton block
\[
 \{w_a\},\{w_{a+1}\},\ldots,\{w_{a+L+b+H-2}\}.
\]
Every core offset color is a consecutive interval inside its block.  The
total block length is

\[
 t(L+b+H-1)=M+t(b+H-1)\le W+{W(b+H)\over L}=W+o(W).                \tag{7.11}
\]

The matching makes all \(M\) core middle colors distinct.  Append every
missing band target as one set-valued letter.  Lemma 7.1 bounds their number
by the overflow plus \(\sum_s(N_s-M)_+\).  Now

\[
 {N_{b\pm q}\over W}
 =\prod_{i=0}^{q-1}{b-i\over b+i+1}
 \le \exp\!\left(-{q^2\over2b}\right).                            \tag{7.12}
\]

If \(N_{b\pm q}>M=(1-\delta)W\) and \(\delta\le1/2\), then
\(q<2\sqrt{b\delta}\).  Every positive deficit is at most \(\delta W\);
hence

\[
 \sum_{s=b-H}^{b+H}(N_s-M)_+
 =O\!\left(W\delta(1+\sqrt{b\delta})\right)=o(W).                  \tag{7.13}
\]

Finally append every missing target outside the band.  If
\(X\sim\operatorname{Bin}(2b,1/2)\), the exponential-moment bound
\(\Pr(|X-b|\ge H)\le2e^{-H^2/b}\), together with
\(W\ge2^{2b}/(2b+1)\), shows that their number is \(o(W)\).
This proves the upper bound.

For the lower bound, the interval unions ending at one word position form a
chain, so at most one middle target can be assigned to that ending position.
All \(W\) middle targets therefore require at least \(W\) positions.
\(\square\)

At
\[
 L\asymp {b\log b\over\log\log b},\qquad
 H\asymp\sqrt{b\log b},                                          \tag{7.14}
\]
both the serialization term and \(H/L\) are small enough, and (7.4) has
\(K\Delta_2/D_K=o(1)\).  If a matching covers a \(1-\eta\) fraction of
middle vertices by extended tracks, then
\[
 \delta=1-{L\over K}(1-\eta)=O(H/L+\eta).                         \tag{7.15}
\]
Thus it is sufficient to have
\[
 \boxed{\eta=o(b^{-1/3})\quad\hbox{and}\quad
        \sum_{s=b-H}^{b+H}V_s=o(W).}                              \tag{7.16}
\]

The quantitative \(o(b^{-1/3})\) is essential to this compiler: an
unspecified \(o(1)\) unmatched fraction does not control the aggregate
zero-quota deficit in (7.13).

## 8. Exact logical boundary

Theorems 2.1 and 4.1 show that the multirank resources are structured and
that their separate quota polytope is integral.  Theorem 5.1 shows that
independent rounding loses FIFO adjacency.  Theorem 6.1 rules out a
parameter-only nibble or local-lemma conclusion.  Theorem 7.2 reduces Gate C
to the following product-specific statement:

> Select a matching of phase-refined extended tracks which leaves
> \(o(Wb^{-1/3})\) middle vertices uncovered and whose induced
> intersection/union colors have aggregate balanced-quota overflow \(o(W)\).

Neither that statement nor a sufficient conditional expansion theorem is
proved here.  A Greene--Kleitman chain may be used as the internal
representation of each flag column, but Theorem 5.1 shows that grouping a
column does not remove the inter-column FIFO compatibility constraint.
