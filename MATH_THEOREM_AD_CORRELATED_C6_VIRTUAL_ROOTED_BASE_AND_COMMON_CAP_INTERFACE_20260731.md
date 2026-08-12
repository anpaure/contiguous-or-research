# Correlated planted C6 banks: virtual rooted bases and the exact common-cap interface

Date: 2026-07-31  
Lane: AD  
Status: exact composition theorem, exact block-triangular cycle-routing
criterion, and a six-port graphic obstruction. No planted-bank existence,
common-basis selection, two-shore cycle closure, global SCD extension, or
compiler theorem is claimed.

## 0. Verdict

A planted suspended C6 is usually written as the gain-one move

\[
             O_i\longrightarrow N_i,\qquad |O_i|=2,\quad |N_i|=3,
\tag{0.1}
\]

whose resource gain is one missing target atom \(t_i\). Insert \(t_i\)
**virtually**. Then (0.1) is the balanced exchange

\[
                  O_i\cup\{t_i\}\longrightarrow N_i,
                         \qquad 3\longleftrightarrow3 .
\tag{0.2}
\]

Consequently a correlated planted bank and any count-neutral sparse-cycle
rerouters can be tested on one rooted graphic basis. For a fixed old rooted
tree, the simultaneous exchange is legal exactly when its
fundamental-cycle minor is nonsingular over \(\mathbf F_2\). If packet
fundamental paths admit an acyclic dependency order, that minor is block
triangular and the packet determinants multiply.

This is the exact physical cycle-routing interface. It also identifies the
first false shortcut: the fact that both phases of every local C6 are
matchings/forests does not imply that a phase change preserves an exterior
forest.

Once a terminal perfect occurrence matching and an anchor-capped physical
forest have been proved, the local Boolean two-step common cap is automatic.
This does not preserve a preassigned pointwise cap, extend the partial rails
to two global SCDs, prove two-shore anchor-pairing acyclicity, or supply the
downstream maximal-envelope compiler.

## 1. Host and rooted-side notation

Put

\[
 M={2n\choose n},\qquad N={2n\choose {n-1}},\qquad
 P={2n\choose {n-2}},
\]

\[
 K=M-N=\operatorname {Cat}_n,\qquad
 C=M-P=\operatorname {Cat}_{n+1}.
\tag{1.1}
\]

Fix one admissible common basis \(Q\) and the corresponding normalized
four-resource side host. An atom

\[
                         a=(D,V;x,y)
\tag{1.2}
\]

uses one lower colour \(D\), one upper colour \(V\), and the two literal
owner slots at the opposite intermediate corners \(x,y\), where

\[
                         D=x\cap y,\qquad V=x\cup y.
\tag{1.3}
\]

Its labelled physical edge is \(\phi(a)=xy\). Parallel labelled
occurrences remain parallel graphic elements.

Let \(B\) be the anchor bank. A \(P\)-edge physical side forest \(J\) on
the \(N\) side owners has no anchor-free component exactly when there is a
root-edge set

\[
 R\subseteq\{\rho b:b\in B\},\qquad |R|=N-P=C-K,
\tag{1.4}
\]

such that \(J\cup R\) is a spanning tree on the owners together with
\(\rho\).

## 2. Virtual completion converts gain one into a basis exchange

Let \(F\) be a host matching of order \(P-h\). Suppose there are pairwise
resource-disjoint target atoms

\[
                         T=\{t_i:i\in I\},\qquad |I|=h,
\tag{2.1}
\]

such that

\[
                         \operatorname {res}(T)=\Lambda(F).
\tag{2.2}
\]

For every \(i\), suppose the planted C6 record has a two-atom off phase
\(O_i\subseteq F\), a three-atom on phase \(N_i\), and

\[
 \operatorname {res}(N_i)
   =\operatorname {res}(O_i)\mathbin{\dot\cup}
     \operatorname {res}(t_i).
\tag{2.3}
\]

Assume the selected complete packet supports are mutually resource-private.

### Lemma 2.1 (virtual perfect completion)

Define

\[
                       \overline F=F\cup T
\tag{2.4}
\]

and

\[
 F^*=\left(F\setminus\bigcup_iO_i\right)\cup\bigcup_iN_i.
\tag{2.5}
\]

Then \(\overline F\) is a perfect matching of the normalized typed host.
Moreover, \(F^*\) is perfect whenever its listed atoms are pairwise
compatible, and its resource incidence is identical to that of
\(\overline F\). Activation is exactly the balanced exchange

\[
 \bigcup_i\bigl(O_i\cup\{t_i\}\bigr)
              \longrightarrow\bigcup_iN_i.
\tag{2.6}
\]

#### Proof

Equation (2.2) says that \(T\) uses once every resource omitted by \(F\).
Summing (2.3) over the private supports gives

\[
 \begin{aligned}
 \operatorname {inc}(F^*)
 &=\operatorname {inc}(F)-\sum_i\operatorname {inc}(O_i)
                         +\sum_i\operatorname {inc}(N_i)\\
 &=\operatorname {inc}(F)+\sum_i\operatorname {inc}(t_i)
  =\operatorname {inc}(\overline F).
 \end{aligned}
\]

The two sides of (2.6) both have \(3h\) atoms. \(\square\)

The targets are virtual only relative to the deficient body \(F\): they
are ordinary legal host atoms and make \(\overline F\) an honest perfect
matching.

## 3. Exact rooted-basis criterion

Assume \(\phi(\overline F)\) is a \(P\)-edge anchor-capped forest with no
anchor-free component. Choose \(R\) as in (1.4) and put

\[
                         \mathcal T=\phi(\overline F)\cup R.
\tag{3.1}
\]

Then \(\mathcal T\) is a spanning tree. Let \(R^*\) be any candidate
terminal root set of order \(N-P\), and put

\[
                         \mathcal T^*=\phi(F^*)\cup R^*.
\tag{3.2}
\]

Cancel every common labelled edge and define

\[
       A=\mathcal T\setminus\mathcal T^*,\qquad
       E=\mathcal T^*\setminus\mathcal T.
\tag{3.3}
\]

Both candidate sets have \(N\) edges, so \(|A|=|E|\). For \(e\in E\), let
\(C_{\mathcal T}(e)\) be its fundamental cycle over the old tree and define

\[
 X_{A,E}(a,e)=\mathbf 1[a\in C_{\mathcal T}(e)].
\tag{3.4}
\]

### Theorem 3.1 (virtual rooted-basis criterion)

Under the host compatibility in Lemma 2.1,

\[
 F^*\text{ is rooted with root set }R^*
 \quad\Longleftrightarrow\quad
                \det_{\mathbf F_2}X_{A,E}=1.
\tag{3.5}
\]

The statement remains exact when \(A,E\) contain both planted-C6 phase
changes and count-neutral sparse-cycle rerouters. Allowing root-star edges
in (3.3) is necessary when the packet changes which anchor is selected in a
component. Keeping \(R^*=R\) is a valid stronger face, not a WLOG
normalization.

#### Proof

Represent the labelled graphic matroid and row-reduce the columns of the
basis \(\mathcal T\) to the identity. The column of a nonbasis edge \(e\)
is the incidence vector of \(C_{\mathcal T}(e)\). Replacing the basis
columns \(A\) by \(E\) gives another basis exactly when (3.4) is
nonsingular. A graphic basis on the \(N+1\) displayed vertices has \(N\)
edges and is a spanning tree. Removing \(R^*\) leaves a forest in which
every component contains the anchor of its unique former root edge. The
converse is identical in reverse. \(\square\)

Thus endpoint routing is encoded by the fundamental paths of the new edges
through the old rooted tree. Internal packet acyclicity is not a substitute
for (3.5).

## 4. Block-triangular cycle routing

Let

\[
 A=\mathbin{\dot\bigcup}_{i=1}^sA_i,\qquad
 E=\mathbin{\dot\bigcup}_{i=1}^sE_i,\qquad |A_i|=|E_i|,
\tag{4.1}
\]

where a block may be a planted full C6 phase, a sparse
\(\ell\leftrightarrow\ell\) rerouter, or a root correction. Write

\[
                         X_{ij}=X[A_i,E_j].
\tag{4.2}
\]

### Theorem 4.1 (past-directed packet composition)

Suppose the packets can be ordered so that

\[
                         X_{ij}=0\qquad(i>j).
\tag{4.3}
\]

Equivalently, every removed packet edge met by the fundamental path of a
new edge of packet \(j\) belongs to packet \(j\) or an earlier packet. Then

\[
                    \det X=\prod_{i=1}^s\det X_{ii}.
\tag{4.4}
\]

Consequently the simultaneous rooted exchange is legal if and only if all
diagonal packet minors are nonsingular.

#### Proof

Condition (4.3) makes \(X\) block upper triangular. Its determinant is the
product of its diagonal determinants. Apply Theorem 3.1. \(\square\)

Full owner privacy makes all off-diagonal blocks zero, but is stronger than
necessary. Acyclic fundamental-path dependence suffices. If the dependency
graph has a cycle, the global determinant remains exact; cyclic dependence
is not by itself a no-go.

### Proposition 4.2 (internal C6 forests do not compose automatically)

On six labelled ports let

\[
 M_0=\{01,23,45\},\qquad M_1=\{12,34,50\},\qquad
 F_0=\{13,24\}.
\tag{4.5}
\]

Then \(F_0\cup M_0\) is the path

\[
                         0-1-3-2-4-5,
\]

whereas \(F_0\cup M_1\) is the four-cycle

\[
                         1-2-4-3-1
\]

together with the separate edge \(05\). Relative to the old tree, with old
rows \(01,23,45\) and new columns \(12,34,50\), the packet minor is

\[
 X=
 \begin{pmatrix}
 0&0&1\\
 1&1&1\\
 0&0&1
 \end{pmatrix},
                    \qquad \det_{\mathbf F_2}X=0.
\tag{4.6}
\]

#### Proof

The graph decompositions are displayed explicitly. In the old tree, the
fundamental paths for \(12\) and \(34\) meet only the old packet edge
\(23\), while the path for \(50\) meets all three old packet edges. This is
(4.6). \(\square\)

This is a labelled graphic obstruction. It is not asserted that the two
exterior edges simultaneously lie on a palette-perfect Boolean side face.
Its exact role is to refute a proof using only “both phases are forests”.

## 5. Sparse cycles and the fixed outer fibre

The sparse \(2\ell\)-cycle phases use the same lower and upper banks. Hence
they preserve both outer leave vectors pointwise. They change literal
slots, physical routing, and the lower-to-upper pairing/cap map. A rigorous
correlated construction therefore has the order

\[
 \text{fixed }Q
 \to\text{outer-aligned body}
 \to\text{sparse-cycle slot/owner routing}
 \to\text{virtual rooted completion}
 \to\text{C6 activation}.
\tag{5.1}
\]

Sparse cycles cannot create (2.2). Once a routed body \(\widehat F\) has
target leave \(T\), however, \(\widehat F\cup T\) is the correct virtual
basis for Theorems 3.1--4.1. A sparse rerouter may instead be included as a
balanced block in one combined basis exchange. Terminal legality then does
not prove a literal prefix serialization; prefix slot, reserve, and
compiler guards remain separate.

## 6. Exactly what common cap follows

Assume \(F^*\) is perfect, respects owner capacities, and its physical graph
is an anchor-capped linear forest. Orient every path component. If
\(a=(D,V;x,y)\) is oriented from \(x\) to \(y\), put

\[
                   f_0(D)=x,\qquad f_1(D)=y,\qquad \pi(D)=V.
\tag{6.1}
\]

### Lemma 6.1 (automatic local Boolean cap)

The maps \(f_0,f_1\) are injective and satisfy

\[
 D\subset f_j(D)\subset\pi(D),\qquad f_0(D)\ne f_1(D),
\tag{6.2}
\]

\[
 f_0(D)\cap f_1(D)=D,\qquad f_0(D)\cup f_1(D)=\pi(D).
\tag{6.3}
\]

Thus the terminal side matching supplies two opposite intermediate rails
with one common two-step cap map \(\pi\).

#### Proof

Along an oriented path each owner is the tail of at most one edge and the
head of at most one edge, proving the injections. Equations (6.2)--(6.3)
are the diamond identities. Exact lower and upper palette saturation makes
\(\pi\) a bijection between the two outer palettes. \(\square\)

Three stronger conclusions do not follow.

1. A planted C6 changes \(\pi\) on each of its three lower colours. A sparse
   \(2\ell\)-cycle changes \(\pi(D_i)=V_i\) to
   \(\pi'(D_i)=V_{i-1}\). Neither preserves a frozen pointwise cap on its
   edited support.
2. Lemma 6.1 gives partial two-step chain segments, not extensions to two
   global saturated SCDs. The pointwise common-cap condition is exact if
   such SCDs are already supplied; their extension is another problem.
3. A target-to-cell SDR/maximal-envelope compiler uses chronology and
   same-cell constraints absent from the side host. It must be regenerated
   or carried as an explicit terminal guard.

## 7. Two-shore and long-cycle rows remain separate

Apply Theorem 3.1 independently on the upper and lower punctured shores.
Each final rooted side forest induces an anchor-pair matching
\(\mu_-\) or \(\mu_+\). Rooted legality on both shores does not imply their
union is acyclic. The exact additional condition is

\[
 \overline{\mu_+}\text{ is loopless and graphic-independent on }V/\mu_-,
\tag{7.1}
\]

with parallel images retained. Equivalently, if \(\alpha,\delta\) are the
two partial involutions, \(\delta\alpha\) has no periodic orbit on its
iterated domain.

The authenticated strict \(n=3\) face has both shores individually rooted
but four common anchor links, which become four quotient loops. Thus (7.1)
is a literal additional condition.

For the three-sector recursion, one-complement-reset-per-augmented-cycle is
still another exported topology state. Neither (3.5) nor (7.1) installs the
reset, orders long cycles, proves cumulative reserve, or gives a literal
word chronology.

## 8. Conditional composition theorem

### Theorem 8.1 (correlated planting with rooted endpoint routing)

Fix \(n\), an admissible common basis \(Q\), and one shore. Suppose:

1. a serializable sparse-cycle sequence produces a matching \(F\) of order
   \(P-h\) whose complete typed leave is a resource-disjoint target bank
   \(T=\{t_i:i\in I\}\);
2. the planted off phases \(O_i\) lie in \(F\), and (2.5) is a legal host
   matching;
3. the virtual completion \(\overline F=F\cup T\) is an anchor-capped rooted
   side forest, with some root set \(R\);
4. for some terminal root set \(R^*\), the exchange minor in Theorem 3.1 is
   nonsingular; and
5. all guards absent from the typed host and labelled graphic matroid,
   including prefix reserve, protected pointwise caps, and compiler
   chronology, are separately verified when required.

Then activation produces a perfect side matching \(F^*\) of size \(P\), an
anchor-capped rooted physical forest, and the local Boolean common cap of
Lemma 6.1. If the packets obey (4.3), hypothesis 4 is equivalent to
nonsingularity of their diagonal blocks.

For a two-shore recursion, adding (7.1) gives the exact combined physical
forest row. A residual-factor transition still requires its declared
one-reset, reserve, deep-shadow, and compiler conditions.

#### Proof

Lemma 2.1 proves typed-host saturation. Theorem 3.1 proves the rooted row,
and Theorem 4.1 gives its packet factorization. Lemma 6.1 gives the local
cap. Equation (7.1) is the exact two-shore contraction theorem. \(\square\)

## 9. Proved/conditional boundary

The virtual normalization shows that, once body leave and off phases are
aligned, the planted bank is an ordinary rooted-basis exchange. The first
false local-to-global implication is

\[
 \text{“each C6 phase is a forest”}
 \Longrightarrow
 \text{“every planted phase choice preserves the exterior forest”},
\]

refuted by Proposition 4.2.

The first unproved existence condition is stronger: jointly choose \(Q\), a
body record, installed off phases, and target atoms so that the virtual
completion is a rooted side base and its terminal exchange minor is
nonsingular. The arbitrary-\(Q\) near-forest theorem and one-point
common-basis marginals do not supply this correlation.

The following gaps remain explicit:

* survival of all packet/rerouter lower colours under one favourable \(Q\);
* outer target Hall and exact slot-displacement reachability;
* positive-density installation of common off phases;
* a rooted virtual completion and nonsingular mixed C6/sparse-cycle minor;
* two-shore quotient acyclicity and long-cycle/reset routing; and
* global SCD extension, residence/deep shadows, and the terminal compiler.

## 10. Audited inputs

The note uses these frozen files and hashes:

* MATH_THEOREM_CATALAN_SPARSE_FIVE_CYCLE_PHYSICAL_SWITCH_20260731.md:
  719104b056ca9d2b94636643d2799b74dc2d9bc3dc759de08b8a2fc11c813dd3.
* MATH_THEOREM_H2_CATALAN_ROOTED_SIDE_TREE_AND_COMMON_CAP_SCD_GATE_20260731.md:
  6598c04dcd930a331a3bf0ebecd19e4daeb01cbc165bd091586b53ec59172b91.
* MATH_THEOREM_H2_CATALAN_ROOTED_UPPER_AND_LOWER_QUOTIENT_GRAPHIC_GATE_20260731.md:
  2719f2d24a067929ad82767a7bf7b052056bbf8fe260278a3f4c98272ab3a7ee.
* MATH_THEOREM_CATALAN_SUSPENDED_TRANSPARENT_HEX_ABSORBER_AND_BLOCKERS_20260731.md:
  40bbd681c8476a00c4cda52742fbbf733fd5c3c8b740d43d2c0cae77f277a79a.
* MATH_THEOREM_H2_CATALAN_CORRELATED_C6_PLANTING_AND_REROUTER_CUT_20260731.md:
  c4120d4724f3b1fafa46e3c0c35b712ccaa50f41f8a5a35f7d2380c35d3b36a1.
* MATH_THEOREM_CATALAN_C6_ROBUST_TARGET_BANK_AND_ZERO_BOUNDARY_REROUTER_GATE_20260731.md:
  dceb249d0026fdee8707a285767729a13c828ecea290749184541453cb64bc7d.

The determinant calculation in Proposition 4.2 is displayed in full and
requires no finite search. No claim from the closed global JMS route is
used.
