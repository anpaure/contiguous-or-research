# Every rephased upper flag has a disjoint ideal reset host; the remaining gate is physical reset typing

**Date:** 2026-08-07  
**Method:** exact Boolean incidence degrees, Koenig's theorem,
Aharoni--Haxell rainbow matching, and a sparse circulant position schedule  
**Status:** asymptotic ideal-host theorem and exact scope correction.
Whenever the exact ratio \(\rho_{m,d}>2\)—in particular, for all
sufficiently large optimal parameters—every target-disjoint bank of
rephased upper companions can be assigned pairwise-disjoint
rank-\((m-1)\)/rank-\(m\) successor states.  There is
also ample abstract room to place a distinct immediate-successor reset and
a distinct lag-\(d\) reset for every upper occurrence.  What the ordinary
SCD start-rank ledger does not provide is a typing of its reset occurrences
by those central edges and by sufficiently large safe lag envelopes.  The
remaining assertion is one explicit typed-reset matching/hypermatching
cut, not a scalar shortage.

This theorem uses the graph case of the standard Aharoni--Haxell rainbow
matching criterion: if a family \((\mathcal G_f)\) of graph edge sets
satisfies the proof-safe sufficient condition

\[
 \nu\!\left(\bigcup_{f\in X}\mathcal G_f\right)>2(|X|-1)
 \qquad(\varnothing\ne X),
\tag{0.1}
\]

then one can choose one edge from every \(\mathcal G_f\), with all chosen
edges pairwise vertex-disjoint.

## 1. Upper flags and their forced central host edge

Use

\[
 n=2m+1,\qquad t=m-d.
\]

A rephased upper companion has penultimate and top targets

\[
 M\in{[n]\choose t-2},
 \qquad
 U=M\cup\{u\}\in{[n]\choose t-1}.
\tag{1.1}
\]

Call \(f=(M,u)\) its **upper flag**.  In a target-disjoint bank, both the
\(M\)'s and the \(U\)'s are distinct.

If the immediate successor has a depth-\(d\) coatom \(Y\), the suffix
recurrence and the rank-\(m\) owner equation force

\[
 M\subset Y,\qquad u\notin Y,
 \qquad T=Y\cup\{u\}\in{[n]\choose m}.
\tag{1.2}
\]

Equivalently, choose

\[
 B\in{[n]\setminus U\choose d+1}
\tag{1.3}
\]

and put

\[
 Y=M\cup B,
 \qquad
 T=U\cup B=Y\cup\{u\}.
\tag{1.4}
\]

The \((d+1)\)-set \(B=T\setminus U=Y\setminus M\) is the fresh bank in
the **immediate-successor** letter.  The upper endpoint's own owner uses a
different source position, \(d\) steps to its left, and may use a different
fresh \((d+1)\)-set.  These two physical resources must not be conflated.

For each flag \(f\), let \(\mathcal G_f\) be the matching in the central
incidence graph with edges \(YT\) from (1.3)--(1.4).  Distinct \(B\)'s give
distinct \(Y\)'s and distinct \(T\)'s, so \(\mathcal G_f\) really is a
matching.

## 2. Exact degree table

The size of every flag matching is

\[
 \boxed{
 D=|\mathcal G_f|
 ={m+d+2\choose d+1}.}
\tag{2.1}
\]

Indeed,

\[
 |[n]\setminus U|
 =2m+1-(m-d-1)=m+d+2.
\]

Now fix a subfamily \(X\) of upper flags, and retain one coloured copy of
an edge for every flag which offers it.  Thus \(G_X\) is a bipartite
multigraph; parallel copies have the same matching and vertex-cover
semantics as the underlying simple graph.  At a coatom
\(Y\in{[n]\choose m-1}\), an incident flag is determined by its distinct
rank-\((t-2)\) set \(M\subset Y\).  Hence

\[
 d_X(Y)\le {m-1\choose t-2}
 ={m-1\choose d+1}.
\tag{2.2}
\]

At an owner \(T\in{[n]\choose m}\), an incident flag is determined by its
distinct rank-\((t-1)\) top \(U\subset T\).  Hence

\[
 d_X(T)\le {m\choose t-1}
 ={m\choose d+1}.
\tag{2.3}
\]

Therefore the maximum degree of the bipartite graph

\[
 G_X=\bigcup_{f\in X}\mathcal G_f
\]

is at most

\[
 \boxed{\Delta={m\choose d+1}.}
\tag{2.4}
\]

The exact expansion ratio is

\[
 \boxed{
 \rho_{m,d}=\frac D\Delta
 =\frac{{m+d+2\choose d+1}}{{m\choose d+1}}>1.}
\tag{2.5}
\]

At the optimal deadline,

\[
 \log\rho_{m,d}
 =\frac{d^2}{m}+o(1)
 \longrightarrow\frac\pi4,
\]

so

\[
 \rho_{m,d}\longrightarrow e^{\pi/4}=2.19328\ldots .
\tag{2.6}
\]

## 3. Pairwise-disjoint central hosts exist asymptotically

### Theorem 3.1 (ideal rainbow host theorem)

Assume \(\rho_{m,d}>2\).  For every target-disjoint upper-flag family
\(\mathcal F\), there are
choices \(B_f\) such that the coatoms

\[
 Y_f=M_f\cup B_f
\]

are pairwise distinct and the owners

\[
 T_f=U_f\cup B_f
\]

are pairwise distinct.

#### Proof

Fix a nonempty \(X\subseteq\mathcal F\).  Counting coloured edge copies,
the multigraph \(G_X\) has exactly
\(|X|D\) edges.  By Koenig's theorem, its maximum matching number equals
the size of a minimum vertex cover; this remains true with parallel edge
copies.  A vertex covers at most \(\Delta\) coloured copies, so

\[
 \nu(G_X)\ge\frac{|X|D}{\Delta}
 =\rho_{m,d}|X|>2|X|>2(|X|-1).
\tag{3.1}
\]

Condition (0.1) holds.  Aharoni--Haxell therefore selects one edge from
every \(\mathcal G_f\), all vertex-disjoint.  Reading its two endpoints as
\(Y_f,T_f\) proves the theorem. \(\square\)

This is stronger than two separate Hall matchings.  The coatom and owner
choices are coupled by the same \((d+1)\)-set \(B_f\), yet both shores are
simultaneously collision-free.

### Corollary 3.2 (extension to the full scalar reset-bank size)

Let \(S=g-P\) be the ordinary abstract reset count.  For every sufficiently
large parameter, the matching from Theorem 3.1 extends to a matching of
\(S\) central coatom--owner edges.

#### Proof

The complete incidence graph between ranks \(m-1\) and \(m\) has

\[
 {n\choose m-1}(m+2)={n\choose m}m=Wm
\]

edges.  After \(k\) pairwise-disjoint central edges have been selected,
deleting their \(k\) coatom and \(k\) owner endpoints removes at most

\[
 k(m+2)+km=k(2m+2)
\]

incidences.  Hence another disjoint central edge remains whenever

\[
 k<\frac{Wm}{2m+2}.
\]

But \(S/W\to0.044054\ldots<1/2\).  Starting with the \(H\)-edge matching
from Theorem 3.1, greedy extension therefore reaches size \(S\). \(\square\)

Thus even extension to the complete scalar reset-bank cardinality has no
central-resource obstruction.  What remains is to realize these abstract
edges as the literal states of the pre-existing reset occurrences.

## 4. Prospective successor-envelope-filtered comparison

Suppose the immediate-successor position assigned to flag \(f\) has safe
coordinate set

\[
 C_f=P_f\cap\bigcap_{I\ni f}T(I),
\]

in the envelope-aware notation.  The coatom \(Y\) is not the successor
source letter.  To state the indexing exactly, if the upper endpoint is
\(e\) and its successor source position is \(q=e+1\), put

\[
 Z_{e,j}=A_{e-j+1}\cup\cdots\cup A_e.
\]

Then

\[
 M_f=Z_{e,d-1},\qquad U_f=Z_{e,d},
\]

whereas

\[
 Y=Z_{q,d}=M_f\cup A_q,\qquad
 T=Z_{q,d+1}=U_f\cup A_q.
\tag{4.0}
\]

The central edge is determined by the fresh exterior

\[
 B=A_q\setminus U_f,\qquad |B|=d+1.
\]

Thus \(Y=M_f\cup B\) and \(T=U_f\cup B\), but the literal source letter
may be

\[
 A_q=B\cup K,\qquad K\subseteq M_f.
\tag{4.0a}
\]

For an envelope \(C_f\), retain a choice

\[
 B\subseteq C_f\setminus U_f.
\tag{4.1}
\]

only when there exists \(K\subseteq M_f\cap C_f\) for which the actual
letter \(A_q=B\cup K\) has the required phase/state type and preserves
every mandatory-core and coordinatewise positive-hit cut.  Let \(D_f\)
be the number of distinct central edges whose exterior \(B\) passes this
existential literal test.  Multiple legal fillers \(K\) for the same
\(B\) still give one central edge.  The maximum host-vertex loads
(2.2)--(2.4) do not increase.

This is not a menu on a frozen owner occurrence.  If \(T_q\) is also fixed,
then (4.0) forces \(B=T_q\setminus U_f\), and there is at most one central
edge for \(f\) at \(q\).  The family below is prospective: varying \(B\)
is allowed to vary the owner occurrence and its compatible history as well.

### Corollary 4.1 (joint-prospective degree criterion)

If

\[
 \boxed{D_f\ge2\Delta=2{m\choose d+1}
 \qquad(f\in\mathcal F),}
\tag{4.2}
\]

then the filtered flag matchings still possess a full rainbow matching.

#### Proof

For every nonempty \(X\), the filtered union has at least
\(2|X|\Delta\) edges and maximum degree at most \(\Delta\).  Koenig gives
\(\nu\ge2|X|>2(|X|-1)\), so apply (0.1). \(\square\)

Define the exact pointwise exterior threshold

\[
 q_*(m,d):=\min\left\{q:{q\choose d+1}
 \ge2{m\choose d+1}\right\}.
\tag{4.3}
\]

A formally sufficient ideal-universe condition, **provided every displayed
exterior \(B\) admits at least one legal filler \(K\) in (4.0a)**, is

\[
 \boxed{|C_f\setminus U_f|\ge q_*(m,d).}
\tag{4.4}
\]

Under that full-typing hypothesis it gives

\[
D_f\ge2{m\choose d+1}=2\Delta.
\]

Without the filler/type hypothesis, (4.4) is only an envelope aperture and
does not lower-bound \(D_f\).

For a **frozen literal occurrence**, however, this sufficient condition is
vacuous.  Its safe set \(C_f\) is contained in every rank-\(m\) owner
window through that occurrence, hence \(|C_f|\le m\).  Therefore

\[
 |C_f\setminus U_f|\le m,
 \qquad
 D_f\le {m\choose d+1}=\Delta.
\tag{4.5}
\]

But \(q_*(m,d)>m\).  Thus (4.4) can certify the complete ideal universe
before the physical host occurrence is selected, but it cannot certify a
pre-existing envelope.  The literal theorem must choose the flag, host,
and occurrence jointly, or verify the exact filtered rainbow cut directly.

At the optimal deadline,

\[
q_*(m,d)=m+
 \left(\frac{4\log2}{\pi}+o(1)\right)d,
\tag{4.6}
\]

so the complete ideal exterior of size \(m+d+2\) is eventually above
this threshold because \(4\log2/\pi=0.8825\ldots<1\).

For a fixed successor position, the necessary exterior aperture is
\(|C_f\setminus U_f|\ge d+1\).  It is not sufficient unless at least one
such exterior admits a legal filler \(K\).  The exact
fixed-schedule condition is the matching-number cut (0.1) for the filtered
edge families; (4.4) is only an ideal-universe comparison.

The separate lag-\(d\) position needs only a fresh bank

\[
 L_f\subseteq C_f^{\rm lag}\setminus U_f,
 \qquad |L_f|=d+1.
\tag{4.7}
\]

Once distinct lag positions have been assigned, the values \(L_f\) need
not be distinct: source letters may repeat.  Thus its exact pointwise gate
is \(|C_f^{\rm lag}\setminus U_f|\ge d+1\), not the rainbow central-edge
condition.

## 5. The physical successor/lag positions also fit abstractly

Let \(g\) be the merged cyclic endpoint count and let \(H\) be the number
of rephased upper companions.  We need an upper-position set \(E\) such
that the three sets

\[
 E,\qquad E+1,\qquad E-d
\tag{5.1}
\]

are pairwise disjoint.  They will carry respectively the upper endpoints,
their immediate reset successors, and their lag-\(d\) buffer slots.

Form the Cayley graph on \(\mathbb Z_g\) with differences

\[
 \{\pm1,\pm d,\pm(d+1)\}.
\]

It has maximum degree at most six, so a greedy independent set has size at
least \(g/7\).  Any \(E\) inside such an independent set satisfies (5.1).

At the optimal deadline,

\[
 \frac Hg\longrightarrow
 \frac{\theta}{1-e^{-\pi/4}}
 =2.56\ldots\times10^{-5}<\frac17.
\tag{5.2}
\]

Hence for every sufficiently large parameter we can choose \(|E|=H\).
The ordinary unused/reset endpoint count satisfies

\[
 \frac SW\longrightarrow0.044054\ldots,
 \qquad
 \frac HW\longrightarrow0.000013949\ldots,
\]

so in particular \(S>2H\) eventually.  Thus the two reset-position shores
in (5.1) fit with enormous scalar room.  No added position is forced by
the successor/lag geometry itself.

## 6. Why the SCD start-rank ledger still does not imply the host theorem

The SCD ledger determines only the integers

\[
 P,\quad F,\quad S=g-P,
\]

and the start-rank multiplicities of the pieces.  It does **not** attach to
an abstract reset occurrence:

1. a coatom \(Y\);
2. an owner \(T\) with a named entering label \(u=T\setminus Y\);
3. the predecessor suffix state \((M,U)\) and the actual successor
   source letter \(A_q=B\cup K\);
4. a separate lag-position safe set \(C_p\); or
5. the occurrence/state data needed to place them at \(e+1\) and \(e-d\).

This loss of information is real.  For one fixed upper flag \((M,u)\), a
reset bank of any prescribed scalar size can be filled entirely with
central edges whose entering label is not \(u\), provided the requested
size is below the enormous complementary edge supply.  That bank has the
same start-rank count but gives the flag degree zero.  Hence no Hall degree
can be inferred from \(S\) alone.

Theorem 3.1 says that the complete Boolean host universe is sufficient.
It does not say that an already frozen ordinary reset bank contains the
selected edges.

## 7. Exact remaining typed-reset cut

Let \(\mathcal R\) be the actual occurrence-labelled successor-reset bank.
Each \(q\in\mathcal R\) stores the predecessor suffix state

\[
\bigl(M_q,U_q\bigr)
 =\bigl(Z_{q-1,d-1},Z_{q-1,d}\bigr),
\]

the actual source letter \(A_q\subseteq C_q\), and hence the forced central
edge

\[
 Y_q=Z_{q,d}=M_q\cup A_q,\qquad
 \widehat T_q=Z_{q,d+1}=U_q\cup A_q.
\]

It also stores its physical/state type.  Let \(\mathcal P\) be the actual
lag-slot bank, with safe sets \(C_p\).

For a flag \(f=(M_f,u_f)\), a joint host is a pair \((q,p)\) satisfying

\[
 (M_q,U_q)=(M_f,U_f),
 \qquad
 \widehat T_q\setminus Y_q=\{u_f\},
 \qquad A_q\subseteq C_q,
\tag{7.1}
\]

and

\[
 |C_p\setminus U_f|\ge d+1,
\tag{7.2}
\]

together with the required phase/state compatibility.  One then chooses
any lag bank \(L_f\in{C_p\setminus U_f\choose d+1}\).  The positional
schedule places \(q\) at \(e_f+1\) and \(p\) at \(e_f-d\).

The exact remaining object is the 3-partite hypergraph on

\[
 \mathcal F\ \dot\cup\ \mathcal R\ \dot\cup\ \mathcal P
\]

whose hyperedges are the triples satisfying (7.1)--(7.2).  It must have a
matching saturating \(\mathcal F\).  If successor and lag roles are frozen
together as one typed reset packet, use that packet as a single right
vertex and ordinary Hall is exact.  If they remain independent resources,
ordinary separate Hall conditions are insufficient; one needs this joint
matching or an Aharoni--Haxell expansion bound for its complete footprint.

This is the precise global host implication left open by the SCD
start-rank model.

## 8. Verdict

The following rows are now unconditional in the complete Boolean host
universe whenever \(\rho_{m,d}>2\), hence for all sufficiently large
optimal parameters:

\[
\boxed{
\begin{gathered}
\text{all rephased upper flags have simultaneous disjoint ideal}\\
\text{coatom--owner hosts, and their successor/lag positions fit}\\
\text{inside the existing endpoint count with a huge margin.}
\end{gathered}}
\]

The unresolved row is no longer Boolean host supply.  It is the physical
typing/planting statement that the ordinary reset occurrences can be
chosen to realize the rainbow edges and their lag-safe banks in one PBBS
history.  The scalar SCD start-rank census alone cannot prove that row.

This theorem does not prove the typed-reset hypermatching, the adaptive
merged PBBS chart theorem, \(\nu(k)\le B(k)+O(1)\), or exact equality.
