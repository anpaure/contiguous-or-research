# Thread A: exact common-successor lift as a colored Euler flow

Date: 2026-07-28

Status: unconditional characterization theorem and unconditional Hall-29
separation example.  The theorem characterizes the chronology image of
rankwise exchanges, but it does not prove that a hole-free Hall-29 lift
exists.  Residence, upper unions, and the compiler owner-Hall system are
kept as subsequent filters.

Scope correction: this one-sided formulation remains exact for the
unrestricted Hall-29 Johnson chronology.  It is **not** by itself a PBBS
fusion theorem.  PBBS surgery must retain the inseparable upper-union
columns in the two-sided diamond table; that corrected Markov calculus is
developed in
THREAD_A_PBBS_TWO_SIDED_DIAMOND_MARKOV_FUSION_20260728.md.

## 0. Outcome

The separate hypersimplex theorem is exact but not synchronized.  It says
that each eligible depth row can be moved, by symmetric two-block exchanges,
to a hole-free multiset with the prescribed point degrees.  It does not say
that independently chosen endpoints of those exchanges are consecutive
trace rows of one Johnson chronology.

This note proves the missing structural characterization.

1. A fixed-boundary family of lower trace histograms comes from one
   Hamilton path in \(J(k,r)\) if and only if an explicit finite
   de Bruijn digraph admits a nonnegative integral Euler flow satisfying
   linear trace-colour and middle-owner equations and having weakly
   connected support.
2. Relative to a reference chronology, the liftable increment families are
   exactly

   \[
     \delta_q=P_qg,\qquad
     g\in\ker_{\mathbb Z}\binom{B}{O},\qquad x^0+g\ge0,
   \]

   with connected final support.  Thus chronological Markov moves are
   images of circulation moves, not arbitrary rankwise \(2\times2\)
   incidence exchanges.
3. At one adjacent pair of depths, the condition factors into an exact
   colour-constrained Euler transportation problem and explicit Hall cuts.
4. For the Hall-29 point-degree vectors, there are hole-free depth-two and
   depth-three completions, each separately reachable from the actual row
   by two-block exchanges, which violate a necessary chronology cut by at
   least \(555\).  Hence the hypersimplex fibres are strictly larger than
   the common-successor image.

The remaining positive problem is to find *some* hole-free point in the
Hall-29 hypersimplex fibres which satisfies the Euler system.  Once that is
done, residence, the upper tower, and the common compiler owner-Hall
extension must still be checked separately.

## 1. The facet word determines the lower tower

Let \(\Omega\) be a \(k\)-set, let \(2\le r<k\), and put

\[
  N=\binom{k}{r}.
\]

For a Johnson path

\[
  T_0,T_1,\ldots,T_{N-1}\in\binom{\Omega}{r},
\]

write its rank-\((r-1)\) facet word as

\[
  S_i=T_i\cap T_{i+1}\qquad(0\le i\le N-2).
\tag{1.1}
\]

For \(q\ge1\), its lower depth-\(q\) trace is

\[
  L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}
  \qquad(0\le i\le N-q-1).
\tag{1.2}
\]

### Lemma 1.1 (facet reconstruction)

Suppose \(S_0,\ldots,S_{N-2}\) are rank-\((r-1)\) sets satisfying

\[
  |S_i\cap S_{i+1}|=r-2
  \qquad(0\le i\le N-3).
\tag{1.3}
\]

Let \(T_-,T_+\) be rank-\(r\) sets with

\[
  S_0\subset T_-,\qquad S_{N-2}\subset T_+.
\tag{1.4}
\]

Assume that the multiset

\[
 \{T_-,T_+\}\uplus
 \{\,S_{i-1}\cup S_i:1\le i\le N-2\,\}
\tag{1.5}
\]

is exactly one copy of \(\binom{\Omega}{r}\).  Then

\[
 T_0=T_-,\qquad
 T_i=S_{i-1}\cup S_i\ (1\le i\le N-2),\qquad
 T_{N-1}=T_+
\tag{1.6}
\]

is a Hamilton path in \(J(k,r)\), its facet word is the prescribed
\((S_i)\), and

\[
 \boxed{
 L_i^{(q)}
   =\bigcap_{j=0}^{q-1}S_{i+j}.}
\tag{1.7}
\]

Conversely, every Hamilton path whose traces through depth two have the
canonical ranks satisfies (1.3)--(1.7).

#### Proof

Condition (1.3) makes each internal union in (1.5) an \(r\)-set.
Equation (1.5) makes all sets in (1.6) distinct.  Consecutive sets in
(1.6) contain the same \((r-1)\)-set \(S_i\), so their intersection is
exactly \(S_i\); hence they are Johnson adjacent.  The owner multiset
(1.5) proves Hamiltonicity.

Finally,

\[
 \bigcap_{j=0}^{q-1}S_{i+j}
 =\bigcap_{j=0}^{q-1}(T_{i+j}\cap T_{i+j+1})
 =\bigcap_{h=0}^{q}T_{i+h},
\]

which is (1.7).  Conversely, a canonical depth-two trace has rank
\(r-2\), so two consecutive facets have intersection rank \(r-2\).
The remaining identities are immediate from (1.1). \(\square\)

Lemma 1.1 is only a lower-tower statement.  It does not infer upper-union
coverage or two-sided residence from lower intersections.

## 2. A fixed-endpoint de Bruijn--Euler theorem

Fix \(H\ge2\).  Let \(\mathscr D_H\) be the directed graph defined as
follows.

* A state is a word

  \[
    u=(S_0,\ldots,S_{H-2})
  \]

  of \(H-1\) rank-\((r-1)\) sets satisfying (1.3) at every adjacent
  pair.
* An arc is a word

  \[
    e=(S_0,\ldots,S_{H-1})
  \]

  of \(H\) such facets, directed from its length-\((H-1)\) prefix to
  its length-\((H-1)\) suffix.

Give an arc the owner colour

\[
 \tau(e)=S_{H-2}\cup S_{H-1}
\tag{2.1}
\]

and, for \(1\le q\le H\), the suffix trace colour

\[
 \lambda_q(e)=\bigcap_{j=H-q}^{H-1}S_j.
\tag{2.2}
\]

Trace colours are regarded as elements of the full Boolean lattice, not
only of the expected rank.  This makes wrong-rank windows visible.

For an initial state \(u=(S_0,\ldots,S_{H-2})\), define its boundary
trace multiset

\[
 \Beta_q(u)=
 \sum_{j=0}^{H-q-1}
 \left[\bigcap_{h=0}^{q-1}S_{j+h}\right]
 \qquad(1\le q\le H),
\tag{2.3}
\]

where the sum is empty for \(q=H\).  Define its internal owner boundary

\[
 \Theta(u)=
 \sum_{j=1}^{H-2}[S_{j-1}\cup S_j].
\tag{2.4}
\]

Let \(B\) be the out-minus-in state--arc incidence matrix of
\(\mathscr D_H\).  Let \(O\) and \(P_q\) be the owner- and trace-colour
matrices

\[
 O_{T,e}=\mathbf1_{\{\tau(e)=T\}},\qquad
 (P_q)_{A,e}=\mathbf1_{\{\lambda_q(e)=A\}}.
\tag{2.5}
\]

### Theorem 2.1 (exact fixed-boundary chronology lift)

Fix endpoint owners \(T_-,T_+\), an initial state \(u\), and a terminal
state \(v\), with the first facet of \(u\) contained in \(T_-\) and the
last facet of \(v\) contained in \(T_+\).  Let \(M_q\) be prescribed
trace multisets for \(1\le q\le H\).

There is a Hamilton path through all rank-\(r\) owners, with these full
boundary states and trace rows \(M_q\), if and only if there is

\[
 x\in\mathbb Z_{\ge0}^{E(\mathscr D_H)}
\]

such that

\[
 Bx=\mathbf e_u-\mathbf e_v,
\tag{2.6}
\]

\[
 [T_-]+[T_+]+\Theta(u)+Ox
   =\mathbf1_{\binom{\Omega}{r}},
\tag{2.7}
\]

\[
 \Beta_q(u)+P_qx=M_q
 \qquad(1\le q\le H),
\tag{2.8}
\]

and all states incident with positive \(x\), together with \(u,v\), lie
in one weakly connected component.

If every \(M_q\) is supported on rank \(r-q\), the resulting lower tower
has the canonical rank at every depth through \(H\).  No upper-union or
compiler-owner assertion is included.

#### Proof

Given a Hamilton path, form its facet word (1.1).  Its consecutive
length-\(H\) windows give \(N-H\) arcs of \(\mathscr D_H\).  Their
multiplicity vector \(x\) has the Euler divergence (2.6).  The initial
state contributes the first \(H-q\) depth-\(q\) windows, while each arc
contributes the unique suffix window ending at its final facet.  Hence
(2.8) counts

\[
 (H-q)+(N-H)=N-q
\]

trace occurrences, exactly the full depth-\(q\) row.  Similarly,
\(\Theta(u)\) contains the first \(H-2\) internal owners and every arc
contributes its last adjacent-facet union.  With the two endpoint owners,
(2.7) counts

\[
 2+(H-2)+(N-H)=N
\]

owners.  The actual arc trail proves weak connectivity.

Conversely, (2.6) and weak connectivity are precisely the hypotheses of
the directed Euler-trail theorem.  Order the arc multiset in an Euler
trail from \(u\) to \(v\).  Overlap of consecutive states produces one
facet word of length

\[
 (H-1)+(N-H)=N-1.
\]

Equation (2.7), followed by Lemma 1.1, reconstructs a Hamilton Johnson
path with endpoints \(T_-,T_+\).  The same boundary/suffix partition of
all \(q\)-windows proves (2.8). \(\square\)

The phrase “fixed boundary” in Theorem 2.1 means the full initial and
terminal length-\((H-1)\) facet states, not merely the two endpoint
middle owners.

### Corollary 2.2 (cyclic version)

For a cyclic Johnson successor factor, use cyclic facet windows, delete
the boundary terms, and replace (2.6) by \(Bx=0\).  The owner equation
\(Ox=\mathbf1\) and the trace equations \(P_qx=M_q\) are exact.  Weakly
connected positive support is equivalent to one Hamilton cycle; without
it the flow gives a successor cycle factor.

## 3. Exact increment image and chronological Markov moves

Fix a reference chronology \(x^0\) and keep its full boundary states and
endpoint owners fixed.  Write

\[
 A_0=\binom{B}{O}.
\tag{3.1}
\]

### Theorem 3.1 (noncircular common-successor increment criterion)

A family of signed rankwise increments

\[
 \delta_q=M_q-M_q^0\qquad(1\le q\le H)
\]

comes from one new Hamilton Johnson chronology with the same full boundary
states if and only if there is an integer vector \(g\) such that

\[
 \boxed{
 g\in\ker_{\mathbb Z}A_0,\qquad
 x^0+g\ge0,\qquad
 P_qg=\delta_q\quad(1\le q\le H),}
\tag{3.2}
\]

and the positive support of \(x^0+g\) is weakly connected.

#### Proof

Subtract (2.6)--(2.8) for the two chronologies.  The fixed boundary terms
cancel, giving (3.2).  Conversely, \(x=x^0+g\) satisfies every equation
of Theorem 2.1; its support hypothesis supplies the Euler trail.
\(\square\)

Thus only the final signed histogram increments matter.  A chosen
decomposition of \(\delta_q\) into rankwise symmetric two-block exchanges
does not itself carry chronological information.

The Graver basis \(\mathcal G(A_0)\) is a finite universal Markov basis
for the nonnegative integral fibre of locally legal successor flows.  A
conformal decomposition of \(g\) into elements of \(\mathcal G(A_0)\)
keeps every intermediate flow nonnegative.  It does **not** follow that
the intermediate supports remain connected, nor that the Graver moves
have bounded support as \(k,H\) grow.  Hence this is an exact factor-fibre
Markov basis, not automatically a Hamilton-fibre Markov basis.

## 4. The first cross-depth Euler and Hall constraints

The full de Bruijn system has a useful two-row projection.

Let \(c_X\) be a prescribed multiplicity vector on rank-\(s\) sets and
let \(d_R\) be a prescribed multiplicity vector on rank-\((s-1)\) sets.
Fix first and last rank-\(s\) terms \(F,L\).

### Theorem 4.1 (pair-row coloured Euler theorem)

There is a Johnson path \(X_0,\ldots,X_{\ell-1}\), with first term \(F\),
last term \(L\), vertex histogram \(c\), and intersection-colour
histogram \(d\), if and only if there are nonnegative integers

\[
 x_{XY}\qquad
 (X,Y\in\binom{\Omega}{s},\ |X\cap Y|=s-1)
\]

such that

\[
 \sum_Yx_{XY}=c_X-\mathbf1_{\{X=L\}},
\qquad
 \sum_Yx_{YX}=c_X-\mathbf1_{\{X=F\}},
\tag{4.1}
\]

\[
 \sum_{X\cap Y=R}x_{XY}=d_R,
\tag{4.2}
\]

and the positive directed multigraph has weakly connected support.

#### Proof

A path gives its directed transition counts.  Conversely, (4.1) gives
Euler divergence \(+1\) at \(F\), \(-1\) at \(L\), and zero elsewhere;
weak connectivity gives one Euler trail.  Its visited vertex and edge
colour counts are (4.1)--(4.2). \(\square\)

### Corollary 4.2 (cross-depth Hall cuts)

For every family \(\mathcal A\) of rank-\((s-1)\) targets, every such
path satisfies

\[
 \sum_{R\in\mathcal A}d_R
 \le
 \sum_{\substack{X:\exists R\in\mathcal A\\R\subset X}}
 \bigl(c_X-\mathbf1_{\{X=L\}}\bigr),
\tag{4.3}
\]

and the analogous inequality with \(F\) in place of \(L\).
In particular,

\[
 \boxed{
 d_R\le\sum_{X\supset R}c_X}
\tag{4.4}
\]

is a necessary singleton cut.

#### Proof

Charge a transition coloured by \(R\in\mathcal A\) to its left endpoint.
Each left occurrence is charged at most once and contains its transition
colour.  This proves (4.3); charging right endpoints gives the second
version. \(\square\)

### Theorem 4.3 (exact two-shore transportation factorization)

Ignoring the final connected-support requirement, equations
(4.1)--(4.2) are feasible if and only if there are nonnegative integers
\(u_{X,R},v_{X,R}\), indexed by \(R\subset X\), such that

\[
 \sum_{R\subset X}u_{X,R}
   =c_X-\mathbf1_{\{X=L\}},
\qquad
 \sum_{R\subset X}v_{X,R}
   =c_X-\mathbf1_{\{X=F\}},
\tag{4.5}
\]

\[
 \sum_{X\supset R}u_{X,R}
  =\sum_{X\supset R}v_{X,R}
  =d_R,
\tag{4.6}
\]

and

\[
 \boxed{u_{X,R}+v_{X,R}\le d_R
        \qquad(R\subset X).}
\tag{4.7}
\]

For a cyclic word, replace the two row sums in (4.5) by \(c_X\).

#### Proof

Given \(x\), let \(u_{X,R}\) count outgoing transitions from \(X\)
with colour \(R\), and let \(v_{X,R}\) count incoming ones.  This gives
(4.5)--(4.6).  A transition of colour \(R\) joins two *distinct*
rank-\(s\) supersets of \(R\), so no occurrence can contribute both to
the outgoing and incoming demand of the same \(X\).  This gives (4.7).

Conversely, fix \(R\).  Its rank-\(s\) supersets form the two shores of a
complete bipartite graph with the diagonal deleted.  Seek a matrix whose
row sums are \(u_{\cdot,R}\), whose column sums are
\(v_{\cdot,R}\), and whose diagonal is zero.  A singleton row type \(X\)
has capacity \(d_R-v_{X,R}\), giving exactly (4.7).  Any set of at least
two row types sees every column type, so it has the full capacity \(d_R\).
These are all Hall cuts.  Integral max flow therefore gives an integral
zero-diagonal matrix.  Combining the matrices over \(R\) gives \(x\).
\(\square\)

Theorem 4.3 gives a cycle decomposition or a path plus cycles.  One word
requires that the per-colour matrices can be chosen with weakly connected
combined support.

## 5. Hall-29: hypersimplex feasibility is strictly insufficient

For Hall-29,

\[
 (k,r,N,H)=(15,8,6435,3).
\]

Write \(M_2,M_3\) for the rank-six and rank-five lower trace rows.  A
hole-free completion has

\[
 M_2^*=\binom{[15]}6\uplus E_2^*,
 \qquad |E_2^*|=e_2=1428,
\tag{5.1}
\]

\[
 M_3^*=\binom{[15]}5\uplus E_3^*,
 \qquad |E_3^*|=e_3=3429.
\tag{5.2}
\]

The exact excess point-degree vectors satisfy

\[
 568\le\gamma_{2,x}\le574,\qquad
 1138\le\gamma_{3,x}\le1147.
\tag{5.3}
\]

### Theorem 5.1 (strict Hall-29 nonliftability inside the marginal fibres)

There are hole-free \(M_2^*,M_3^*\) satisfying the exact Hall-29 point
degrees such that each row is separately connected to the actual Hall-29
row by symmetric two-block exchanges, but the pair
\((M_2^*,M_3^*)\) is not the pair of consecutive lower rows of any
Johnson chronology.

Indeed the singleton cut (4.4) can fail by at least \(555\).

#### Proof

Fix any five-set \(R\), and put

\[
 t=\min_{x\in R}\gamma_{3,x}.
\]

Then \(1138\le t\le1147\).  Prescribe \(t\) excess copies of \(R\) and
put

\[
 d'_x=\gamma_{3,x}-t\,\mathbf1_{\{x\in R\}},
\qquad e'=e_3-t.
\tag{5.4}
\]

The checksum is

\[
 \sum_xd'_x=5e'.
\]

For \(x\in R\), \(0\le d'_x\le9\).  For \(x\notin R\),
\(d'_x\le1147\), while

\[
 e'\ge3429-1147=2282.
\]

Thus \(0\le d'_x\le e'\) for every \(x\).  The integer decomposition
theorem for the hypersimplex supplies \(e'\) further five-blocks with
degree vector \(d'\).  Consequently there is a valid excess design
\(E_3^*\) containing at least \(t\) copies of \(R\), and therefore

\[
 M_3^*(R)\ge1+t\ge1139.
\tag{5.5}
\]

Now take any hole-free \(M_2^*\) with excess degree vector \(\gamma_2\).
Exactly ten six-sets contain \(R\).  Every excess six-block containing
\(R\) contributes to the degree of every \(x\in R\), so their number is
at most

\[
 \min_{x\in R}\gamma_{2,x}\le574.
\]

Hence

\[
 \sum_{X\supset R}M_2^*(X)\le10+574=584.
\tag{5.6}
\]

In a chronology, every occurrence of the depth-three target \(R\) is the
intersection of two consecutive depth-two occurrences, each containing
\(R\).  Charging it to the left occurrence gives the necessary inequality

\[
 M_3(R)\le\sum_{X\supset R}M_2(X).
\tag{5.7}
\]

Equations (5.5)--(5.6) violate (5.7) by at least
\(1139-584=555\).

Finally, both constructed rows have the same cardinalities and point
degrees as their actual Hall-29 counterparts.  Rankwise quadratic
generation therefore connects each actual row to its constructed
endpoint by symmetric two-block exchanges. \(\square\)

Theorem 5.1 is not a counterexample to the existence of a common
hole-free Hall-29 lift.  It proves that the hypersimplex completions must
be chosen jointly: many individually valid choices are outside the
chronology image.

### Exact Hall-29 chronology audit

Let

\[
 X_i=T_i\cap T_{i+1},\qquad
 Y_i=X_i\cap X_{i+1},\qquad
 Z_i=Y_i\cap Y_{i+1}.
\tag{5.8}
\]

If \(T_{i+1}=T_i-\{a_i\}+\{b_i\}\), the actual Hall-29 arrays satisfy
the coupled diamonds

\[
\begin{array}{lll}
T_i=X_i\cup\{a_i\},&
T_{i+1}=X_i\cup\{b_i\},\\
X_i=Y_i\cup\{a_{i+1}\},&
X_{i+1}=Y_i\cup\{b_i\},\\
Y_i=Z_i\cup\{a_{i+2}\},&
Y_{i+1}=Z_i\cup\{b_i\}.
\end{array}
\tag{5.9}
\]

In particular, the same insertion \(b_i\) drives every depth:

\[
 X_{i+1}=X_i-\{a_{i+1}\}+\{b_i\},
\quad
 Y_{i+1}=Y_i-\{a_{i+2}\}+\{b_i\},
\quad
 Z_{i+1}=Z_i-\{a_{i+3}\}+\{b_i\}.
\tag{5.10}
\]

In the stored integer-mask notation the fixed endpoint chains are

\[
 9901\supset1709\supset1197\supset173,
\qquad
 7779\supset3683\supset1635\supset1571.
\tag{5.11}
\]

The boundary corrections are

\[
 \epsilon_2=\mathbf e_{12}+\mathbf e_{13},
\qquad
 \epsilon_3=
 2\mathbf e_{13}+\mathbf e_9+\mathbf e_{11}+2\mathbf e_{12}.
\tag{5.12}
\]

These identities are all realized by the actual, holed Hall-29 tower.
The vectors (5.3) and the scalar hole counts alone do not specify any
new \(X,Y,Z\) arrays and therefore cannot check (5.9)--(5.10).

There is also a hierarchy of immediate chronology inequalities.  For a
coordinate subset \(Q\) with \(|Q|\le8\), let \(d_q(Q)\) count
depth-\(q\) traces containing \(Q\), and put

\[
 d_0(Q)=\binom{15-|Q|}{8-|Q|}.
\]

Decomposing the \(Q\)-containment word into one-runs gives

\[
 d_0(Q)-2d_1(Q)+d_2(Q)\ge0,
\qquad
 d_1(Q)-2d_2(Q)+d_3(Q)\ge0.
\tag{5.13}
\]

The two left sides count, respectively, the length-one and length-two
containment runs.  They constrain all subsets \(Q\), not merely points.

## 6. Odd-graph successors require the odd square-root cocycle

Theorems 2.1 and 3.1 are exact for an unrestricted Johnson chronology.
They do not by themselves prove that its successor is the square of an
odd-graph successor.

For a Johnson edge \(B_iB_{i+1}\) in \(J(2m+1,m)\), put

\[
 N_i=[2m+1]\setminus(B_i\cup B_{i+1}).
\tag{6.1}
\]

Even if the \(N_i\) form a permutation of the middle layer, an odd
successor \(\sigma\) with \(B_{i+1}=\sigma^2(B_i)\) requires the stronger
rooted cocycle.  If \(N_i=B_{f(i)}\), then

\[
 \boxed{f^2(i)=i+1.}
\tag{6.2}
\]

The clean exact automaton therefore works directly in the odd graph.
Its arcs are legal windows

\[
 (A_0,A_1,\ldots,A_{2H}),
\qquad A_j\cap A_{j+1}=\varnothing,
\tag{6.3}
\]

and its states are their length-\(2H\) prefix and suffix.  Give such an
arc owner \(A_0\) and depth-\(q\) colour

\[
 \bigcap_{h=0}^{q}A_{2h}.
\tag{6.4}
\]

If \(B_{\rm odd},O_{\rm odd},P_q^{\rm odd}\) are the resulting incidence,
owner, and colour matrices, then

\[
 z\ge0,\qquad
 B_{\rm odd}z=0,\qquad
 O_{\rm odd}z=\mathbf1,\qquad
 P_q^{\rm odd}z=M_q
\tag{6.5}
\]

is exactly an odd-graph successor factor with the prescribed full
even-step flag tower.  Connected selected support is exactly one
odd-graph Hamilton cycle.  Relative increments have the same kernel form
as (3.2), with the odd matrices.

#### Proof

An odd successor selects one length-\((2H+1)\) window beginning at every
middle owner, so (6.5) is necessary.  Conversely,
\(O_{\rm odd}z=\mathbf1\) makes every selected arc multiplicity binary.
Flow conservation shifts each selected window to its unique continuation,
producing a disjoint union of odd-graph successor cycles.  The colour
equations are exactly (6.4), and weak connectivity makes the union one
cycle. \(\square\)

This odd-window formulation, rather than a merely bijective list of
missing labels \(N_i\), preserves the square-successor cocycle.

## 7. Exact proved/open boundary

The common-successor *characterization* is now complete:

* unrestricted Johnson paths are exactly the fixed-boundary Euler flows
  of Theorem 2.1;
* fixed-boundary increment families are exactly the kernel image (3.2);
* odd-graph successors are exactly the odd-window flows (6.5); and
* the first adjacent-depth projection has the exact transportation and
  Hall description of Theorems 4.1--4.3.

What is not proved is feasibility of a desired hole-free point in this
integer flow fibre.  For Hall-29 the smallest chronology-only problem is:

> Choose hole-free \(M_2,M_3\) with the forced hypersimplex degree vectors,
> together with \(M_1\), so that the fixed-boundary system
> (2.6)--(2.8) has a weakly connected integral solution.

Only after this succeeds should one impose:

1. the residence exclusions not already forced by the prescribed
   correct-rank lower rows, including the required two-sided tests;
2. complete upper-union support; and
3. the separate common compiler owner-Hall extension.

The middle-owner equation (2.7) is intrinsic Hamilton-path ownership and
must not be confused with item 3.  The Hall-29 separation theorem shows
that no argument using only cardinalities, point degrees, or independent
rankwise two-block connectivity can solve the chronology-only problem.
