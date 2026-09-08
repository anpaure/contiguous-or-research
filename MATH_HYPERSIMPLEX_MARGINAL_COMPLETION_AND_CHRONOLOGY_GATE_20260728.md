# Hypersimplex completion removes every rankwise hole: chronology is the only coupling gate

Date: 2026-07-28

Status: unconditional marginal theorem, followed by an exact numerical
specialization to the frozen `k=15` Hall-29 carrier.  It does not construct a
new chronology.

## 0. Outcome

For a resident middle chronology, the cross-depth transport law prescribes
the point degrees of every lower trace multiset.  Those degree constraints do
**not** force any holes.  Whenever the obvious coordinate bounds hold, the
prescribed excess vector is an integer point of a dilated hypersimplex and
therefore decomposes into uniform blocks.  Adding one copy of every target
produces a hole-free multiset with exactly the required size and point
degrees.

Consequently, every existing depth row can be transformed marginally into a
hole-free row by symmetric two-block exchanges.  The unresolved theorem is
exactly the lift of those exchanges to one middle transition word,
simultaneously at every depth and compatibly with the owner compiler.

At `k=15`, the Hall-29 first-shadow data prescribe hole-free depth-two and
depth-three excess degrees lying respectively in `[568,574]` out of `1428`
and `[1138,1147]` out of `3429`.  Thus the large marginal feasibility margins
are explicit.

## 1. Integer decomposition of the hypersimplex

### Lemma 1.1 (uniform multidesign realization)

Let `n,e,s` be nonnegative integers with `s<=n`, and let

\[
 d=(d_1,\ldots,d_n)\in\mathbb Z^n
\]

satisfy

\[
 0\le d_x\le e\quad(1\le x\le n),
 \qquad \sum_xd_x=se.
 \tag{1.1}
\]

Then there is a multiset `E` of exactly `e` subsets of `[n]`, each of size
`s`, whose point-degree vector is `d`.

#### Proof

Induct on `e`.  The case `e=0` is immediate.  Let

\[
 M=\{x:d_x=e\}.
\]

Equation (1.1) gives `|M|<=s`.  There are at least `s` positive coordinates:
otherwise their total would be at most `(s-1)e`.  Choose an `s`-set `A`
containing `M` and otherwise using positive coordinates.  Put

\[
 d'=d-\mathbf1_A.
\]

Every coordinate of `d'` lies in `[0,e-1]`: positivity protects the lower
bound, while every coordinate equal to `e` was forced into `A`.  Moreover

\[
 \sum_xd'_x=s(e-1).
\]

Apply induction to `d'` and append `A`.  \(\square\)

Equivalently, the uniform-matroid base polytope

\[
 \{x\in[0,1]^n:\sum_xx_i=s\}
\]

has the integer decomposition property.  The elementary proof above is all
that is needed here.

## 2. Application to a synchronized Johnson tower

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be a depth-`d` resident Hamilton path in `J(k,r)`, and let

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}
 \qquad(0\le i<W-q).
 \tag{2.1}
\]

Write `H_q` for the hole set and `E_q` for the repeat multidesign of the
rank-`r-q` trace row.  Retain the notation of the exact defect-transport law:

\[
 \Delta=\binom{k-1}{r-1}-\binom{k-1}{r-2},
 \tag{2.2}
\]

\[
 \beta_q=\binom{k-1}{r-1}
          -\binom{k-1}{r-q-1}-q\Delta,
 \tag{2.3}
\]

and let `epsilon_(q,x)` be the boundary-run correction.  Define

\[
 \gamma_{q,x}
 =\beta_q-q\bigl(\deg_{H_1}(x)-\deg_{E_1}(x)\bigr)
   +\epsilon_{q,x}.
 \tag{2.4}
\]

Finally put

\[
 s_q=r-q,\qquad
 N_q=\binom{k}{s_q},\qquad
 e_q=W-q-N_q.
 \tag{2.5}
\]

The scalar defect ledger says `|E_q|-|H_q|=e_q`, while the pointwise law
says

\[
 \deg_{E_q}(x)-\deg_{H_q}(x)=\gamma_{q,x}.
 \tag{2.6}
\]

### Theorem 2.1 (rankwise zero-hole completion)

Fix `q<=d`.  If

\[
 0\le\gamma_{q,x}\le e_q\qquad(x\in[k]),
 \tag{2.7}
\]

then there exists a multiset `M_q^*` of exactly `W-q` rank-`s_q` sets such
that

1. every rank-`s_q` target occurs at least once;
2. `M_q^*` has the same point-degree vector as the actual trace multiset
   `(L_i^(q))`;
3. the actual trace multiset and `M_q^*` are connected by symmetric
   two-block exchanges.

#### Proof

Summing (2.6) over points and using the scalar ledger gives

\[
 \sum_x\gamma_{q,x}=s_qe_q.
 \tag{2.8}
\]

Apply Lemma 1.1 with `n=k`, `s=s_q`, `e=e_q`, and degree vector
`gamma_q`.  It supplies an excess multidesign `E_q^*` of `e_q` blocks.
Define

\[
 M_q^*=\binom{[k]}{s_q}\uplus E_q^*.
 \tag{2.9}
\]

This multiset has `N_q+e_q=W-q` blocks and no holes.  Its point degrees are

\[
 \binom{k-1}{s_q-1}+\gamma_{q,x},
\]

which equal the actual trace degrees by (2.6).  The two multisets therefore
have the same block count, uniform block size, and point degrees.  The
alternating-cycle decomposition of their incidence bipartite graphs
transforms one into the other by `2 x 2` switches, equivalently symmetric
two-block exchanges.  \(\square\)

### Corollary 2.2 (no rankwise obstruction)

Under (2.7), holes at depth `q` cannot be certified by any argument using
only total multiplicity, point degrees, or the complete rankwise exchange
lattice.  Any genuine obstruction must use at least one of:

1. synchronization of the exchanges across different `q`;
2. liftability to one Johnson chronology and its residence word;
3. upper-shadow occurrence survival;
4. the common owner/Hall realization of the literal compiler.

This is stronger than saying that two already feasible designs with the same
degrees are exchange-connected: it explicitly constructs a feasible
degree-matched design with **zero holes**.

## 3. Exact `k=15` specialization

For the frozen Hall-29 chronology,

\[
 (k,r,W,d)=(15,8,6435,3),
\]

and the first-shadow defects are

\[
 H_1=\{5801,7267,8877,13620\},
\]

\[
 E_1=\{17140,3868,4525\}.
\]

Direct evaluation of (2.4), including the two boundary corrections, gives

\[
 e_2=1428,
\]

\[
 (\gamma_{2,x})_{x=0}^{14}
 =(568,570,574,572,574,568,572,572,574,572,568,572,569,569,574),
 \tag{3.1}
\]

and

\[
 e_3=3429,
\]

\[
 (\gamma_{3,x})_{x=0}^{14}
 =(1138,1141,1147,1144,1147,1138,1144,1144,1147,1145,
   1138,1145,1140,1140,1147).
 \tag{3.2}
\]

The checksums are

\[
 \sum_x\gamma_{2,x}=6\cdot1428=8568,
 \qquad
 \sum_x\gamma_{3,x}=5\cdot3429=17145.
\]

Both vectors lie very far inside their hypersimplex bounds.  Theorem 2.1
therefore gives:

* a hole-free rank-six multiset with exactly the point degrees forced at
  depth two; and
* a hole-free rank-five multiset with exactly the point degrees forced at
  depth three.

The observed `21` and `4` holes are thus entirely chronological.  They are
not forced by Catalan regularity, boundary degrees, scalar capacity, or the
rankwise trade lattice.

## 4. The sharpened common target

The marginal completion can be performed separately for every depth.  What
is missing is one sequence of transition deletions and insertions whose
induced exchange at depth `q` realizes the selected `M_q^*` for all `q` at
once.  In the deletion-chain notation,

\[
 L_i^{(q)}=T_i\setminus\{a_i,\ldots,a_{i+q-1}\}.
\]

Hence the exact remaining carrier statement is a **simultaneous
hypersimplex-lift theorem**: lift compatible rankwise two-block exchanges to
one exchange of the deletion word, preserving residence and the upper flag
tower.  The exact finite formula additionally requires the resulting nested
rows to admit one trace-two owner extension.

This separates two questions which had repeatedly been conflated:

* marginal balancing is solved by Lemma 1.1;
* chronological and owner compatibility remain open.

