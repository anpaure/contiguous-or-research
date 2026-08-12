# Fixed-pair target orbits, cube direction words, and the exact resolution assignment

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Fix a partition of the \(2m\) Boolean coordinates into pairs
\[
                         P_i=\{a_i,b_i\},\qquad i\in[m].       \tag{0.1}
\]
Let
\[
                         G=C_2^m\rtimes S_m                 \tag{0.2}
\]
be the full group preserving this unordered pair decomposition.

The \(G\)-orbits on rank-\(m-q\) targets are indexed by one integer \(f\):
\[
\boxed{
\begin{array}{c|ccc}
 &\text{full}&\text{empty}&\text{split}\\ \hline
\mathcal O^-_{f,q}&f&f+q&m-2f-q .
\end{array}}                                             \tag{0.3}
\]
Their sizes are
\[
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.             \tag{0.4}
\]
Complementation gives the upper orbit
\[
\mathcal O^+_{f,q}:
\qquad(f+q)\text{ full},\quad f\text{ empty},\quad
      m-2f-q\text{ split}.                              \tag{0.5}
\]

A fixed lower target of type \((f,q)\) has
\[
                              \binom{m+q}{q}              \tag{0.6}
\]
unrestricted middle extensions.  Its fixed-pair-compatible extensions,
meaning middle vertices in a \(q\)-face whose intersection is the target,
number exactly
\[
                         \boxed{
                         2^q\binom{f+q}{q}.}              \tag{0.7}
\]
The factors are respectively the choice of the \(q\) empty pairs to make
free and the two starting orientations of each free pair.

Every source middle stratum has
\[
                         f\text{ full},\quad f\text{ empty},\quad
                         h=m-2f\text{ split},             \tag{0.8}
\]
and is an orientation cube \(Q_h\).  If a directed cube cycle has vertex
word \(\eta_t\) and direction word \(w_t\), then its length-\(q\) window
covers a lower target \(T=(F,E,S,\theta)\) exactly when

1. \(w_t,\ldots,w_{t+q-1}\) are distinct;
2. their set is \(D\subset E\), \(|D|=q\);
3. the source fibre is
   \[
   (F,E\setminus D,S\cup D);
   \]
4. \(\eta_t|_S=\theta\).

The upper target covered by the same window is obtained by making the
pairs in \(D\) full instead of empty.

Finally, choosing one resolution class in every \(Q_h\)-fibre is exactly
a multiple-choice \(0\)-\(1\) system.  Its typewise rank-balance equations
are
\[
 \boxed{
 \sum_{\alpha\in\mathfrak F_f}
 \sum_{\rho\in\mathscr R_{m-2f}}
       n_{\rho,\ge q}\,x_{\alpha,\rho}
       =T_{f,q}.}                                      \tag{0.9}
\]
Here \(\mathfrak F_f\) is the set of type-\(f\) middle fibres,
\(x_{\alpha,\rho}\) chooses resolution \(\rho\) in fibre \(\alpha\), and
\(n_{\rho,\ge q}\) counts its vertices assigned radius at least \(q\).
The complete labelled system replaces (0.9) by one lower and one upper
incidence equation for every individual target.

Equation (0.9) makes the fixed-frame obstruction immediate: its left side
is nested and is at most the number \(V_f\) of type-\(f\) middle owners,
while the required sequence \(T_{f,q}\) can increase with \(q\) and has a
positive Gaussian excess over \(V_f\).  Thus the assignment problem is
the exact fixed-frame formulation, but it has no coefficient-one solution
through the required band.  Mixing pair frames changes the incidence
matrix and is mandatory.

## 1. Complete orbit classification

For a subset \(T\subseteq[2m]\), write
\[
 e(T),\quad f(T),\quad s(T)                              \tag{1.1}
\]
for its numbers of empty, full, and split coordinate pairs.  Then
\[
 e(T)+f(T)+s(T)=m,\qquad |T|=2f(T)+s(T).                \tag{1.2}
\]

If \(|T|=m-q\), subtracting the two equations gives
\[
                              e(T)-f(T)=q.               \tag{1.3}
\]
Hence, on putting \(f=f(T)\),
\[
 e=f+q,\qquad s=m-2f-q,                                 \tag{1.4}
\]
where
\[
                         0\le f\le\left\lfloor
                                   \frac{m-q}{2}\right\rfloor. \tag{1.5}
\]

### Theorem 1.1 (pair-frame orbits)

Two rank-\(m-q\) targets lie in the same \(G\)-orbit if and only if they
have the same number \(f\) of full pairs.  Thus the orbits are exactly
\(\mathcal O^-_{f,q}\) in (0.3).

#### Proof

The numbers of empty, full, and split pairs are invariant under \(G\).
Conversely, a pair permutation sends the three pair-type index sets of
one target to those of the other, and the \(C_2\)-swap in every split pair
then aligns its selected endpoint. \(\square\)

For a target in \(\mathcal O^-_{f,q}\), the stabilizer has order
\[
                       2^{2f+q}\,f!(f+q)!(m-2f-q)!.     \tag{1.6}
\]
Indeed both coordinate swaps fix an empty or full pair, while a split
pair has only the identity swap in its stabilizer.  Since
\(|G|=2^m m!\), orbit--stabilizer gives (0.4).

Summing the orbit sizes recovers the whole rank:
\[
             \sum_fT_{f,q}=\binom{2m}{m-q}.             \tag{1.7}
\]
Complementation interchanges empty and full pairs and proves (0.5) with
the same orbit sizes.

## 2. All middle extensions and their refined types

Fix \(T\in\mathcal O^-_{f,q}\), and let \(E,F,S\) be its empty, full,
and split pair index sets.  A middle extension \(X\supseteq T\) adds
exactly \(q\) coordinates.  Refine such an extension by:

* \(a\): empty pairs receiving both coordinates;
* \(b\): empty pairs receiving exactly one coordinate;
* \(c\): split pairs receiving their missing coordinate.

Then
\[
                              2a+b+c=q.                 \tag{2.1}
\]
For fixed \((a,b,c)\), the exact number of extensions is
\[
 \boxed{
 M_{a,b,c}(f,q)
   =\binom{f+q}{a}
      \binom{f+q-a}{b}2^b
      \binom{m-2f-q}{c}.}                              \tag{2.2}
\]

The resulting middle set has
\[
\begin{aligned}
 f(X)&=f+a+c,\\
 e(X)&=f+q-a-b,\\
 s(X)&=m-2f-q+b-c.
\end{aligned}                                          \tag{2.3}
\]
Equation (2.1) makes the first two quantities equal, as they must at the
middle rank.

Summing (2.2) over \(2a+b+c=q\) gives
\[
 \sum_{2a+b+c=q}M_{a,b,c}(f,q)
   =\binom{2(f+q)+(m-2f-q)}q
   =\binom{m+q}{q},                                     \tag{2.4}
\]
which proves (0.6).

### The fixed-pair face-compatible subfamily

A pair-flip \(q\)-face having intersection \(T\) must make exactly \(q\)
of the empty pairs split at its middle vertices.  It cannot complete a
split pair or make an empty pair full.  Thus
\[
                              (a,b,c)=(0,q,0).           \tag{2.5}
\]
Formula (2.2) becomes (0.7):
\[
                  M_{\mathrm{face}}(T)
                    =2^q\binom{f+q}{q}.                 \tag{2.6}
\]

There are
\[
                              \binom{f+q}{q}             \tag{2.7}
\]
candidate source faces.  After a starting corner and an ordering of the
free directions are specified, the number of directed geodesic witness
paths is
\[
                          2^q q!\binom{f+q}{q}.           \tag{2.8}
\]
Each one contains \(q+1\) distinct middle extensions of \(T\), namely its
consecutive path vertices.  This is the path-hitting interpretation:
coverage is not the availability of one of the \(2^q\) face vertices but
the occurrence of \(q+1\) of them in the correct consecutive order.

## 3. Source orientation-cube fibres

A source middle set has equal numbers \(f\) of full and empty pairs.  Put
\[
                              h=m-2f.                    \tag{3.1}
\]
A labelled source fibre is a triple
\[
                 \alpha=(F_0,E_0,R),\qquad
 |F_0|=|E_0|=f,\quad |R|=h,                              \tag{3.2}
\]
partitioning \([m]\).  Its middle vertices are
\[
 X_\alpha(\eta)
   =\bigcup_{i\in F_0}P_i
      \ \cup\
      \{a_i:\eta_i=0,\ i\in R\}
      \ \cup\
      \{b_i:\eta_i=1,\ i\in R\},
 \qquad \eta\in\mathbb F_2^R.                            \tag{3.3}
\]
Thus the fibre is canonically \(Q_h\).

The number of type-\(f\) fibres is
\[
 B_f=\frac{m!}{f!^2h!}
    =\binom mh\binom{m-h}{f},                            \tag{3.4}
\]
and their total number of vertices is
\[
 V_f=B_f2^h
    =\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.                  \tag{3.5}
\]

For a fixed lower target
\[
 T=(F,E,S,\theta)\in\mathcal O^-_{f,q},                \tag{3.6}
\]
its candidate source fibres are indexed by
\[
                              D\in\binom Eq:             \tag{3.7}
\]
\[
 \alpha_D=(F,E\setminus D,S\cup D).                    \tag{3.8}
\]
Every such fibre has dimension
\[
                        |S|+|D|=m-2f=h.                 \tag{3.9}
\]
Inside \(\alpha_D\), the \(2^q\) extensions in (2.6) are precisely the
vertices of the face
\[
 \{\eta\in Q_h:\eta|_S=\theta\},                        \tag{3.10}
\]
whose free directions are \(D\).

## 4. Coverage by cyclic direction words

Let a directed cycle in \(Q_h\) be
\[
             \eta_0,\eta_1,\ldots,\eta_{\ell-1},\eta_\ell=\eta_0,
                                                               \tag{4.1}
\]
with direction word
\[
             w_t\in R,\qquad
             \eta_{t+1}=\eta_t+e_{w_t}.                \tag{4.2}
\]
Indices below are cyclic.

For a start \(t\) and depth \(q\), put
\[
               W(t,q)=(w_t,\ldots,w_{t+q-1}),\qquad
               D(t,q)=\{w_t,\ldots,w_{t+q-1}\}.         \tag{4.3}
\]

### Proposition 4.1 (direction-word shadow formula)

The \(q+1\) middle vertices
\[
 X_\alpha(\eta_t),\ldots,X_\alpha(\eta_{t+q})          \tag{4.4}
\]
form a Johnson geodesic if and only if the letters of \(W(t,q)\) are
distinct.  In that case their intersection and union are
\[
 L_{\alpha,t,q}
  =\bigcup_{i\in F_0}P_i
     \ \cup\
     \{a_i^{\eta_{t,i}}:i\in R\setminus D(t,q)\},       \tag{4.5}
\]
\[
 U_{\alpha,t,q}
  =L_{\alpha,t,q}\cup\bigcup_{i\in D(t,q)}P_i.          \tag{4.6}
\]
Here \(a_i^0=a_i\) and \(a_i^1=b_i\).

#### Proof

A repeated direction restores a previously changed pair orientation, so
the path is not geodesic.  If all directions are distinct, every direction
is flipped once.  Both endpoints of each flipped pair occur somewhere in
the window, so neither lies in the intersection and both lie in the union.
Every unflipped split pair has one constant selected endpoint.  Full and
empty pairs outside the orientation cube never change.  This gives
(4.5)--(4.6). \(\square\)

### Corollary 4.2 (exact target-hitting criterion)

For the lower target \(T=(F,E,S,\theta)\), a window in the candidate
fibre \(\alpha_D\) covers \(T\) if and only if
\[
\begin{aligned}
 &W(t,q)\text{ has distinct letters},\\
 &D(t,q)=D,\\
 &\eta_t|_S=\theta.
\end{aligned}                                          \tag{4.7}
\]
The orientation of \(\eta_t\) on \(D\) is unrestricted.

Dually, if an upper target has full set \(G\), empty set \(E_0\), split
set \(S\), and split orientation \(\theta\), it is covered precisely in
a fibre
\[
              (G\setminus D,E_0,S\cup D),\qquad
              D\in\binom Gq,                            \tag{4.8}
\]
by a window satisfying the analogue of (4.7).

Thus a direction word, rather than a raw cube face, is the exact coverage
object.

## 5. Resolution classes

Fix a clipped depth \(H\).  A resolution class
\[
                              \rho\in\mathscr R_h        \tag{5.1}
\]
consists of:

1. a directed cycle/path resolution of all vertices of \(Q_h\);
2. its direction word on every component;
3. a clipped radius label
   \[
                           r_\rho:Q_h\to\{0,\ldots,H\}; \tag{5.2}
   \]
4. the legality condition that, whenever \(q\le r_\rho(\eta)\), the next
   \(q\) direction letters from \(\eta\) are distinct.

The class may also record component cuts and phases; these do not change
the incidence equations below.  Put
\[
 n_{\rho,d}=|\{\eta:r_\rho(\eta)=d\}|,\qquad
 n_{\rho,\ge q}=|\{\eta:r_\rho(\eta)\ge q\}|.           \tag{5.3}
\]

For a labelled fibre \(\alpha\), transport \(\rho\) through the canonical
identification (3.3).  Define the exact incidence coefficients
\[
 a^-_{\alpha,\rho,q}(T)
   =\#\{\eta:r_\rho(\eta)\ge q,\
          L_{\alpha,\eta,q}=T\},                        \tag{5.4}
\]
\[
 a^+_{\alpha,\rho,q}(U)
   =\#\{\eta:r_\rho(\eta)\ge q,\
          U_{\alpha,\eta,q}=U\}.                        \tag{5.5}
\]
By Proposition 4.1 every active start contributes one lower and one upper
target of the paired orbit type.

## 6. The exact rank-balanced assignment problem

Let
\[
                         N_q=\binom{2m}{m-q},            \tag{6.1}
\]
and define the clipped SCD radius quotas
\[
 c_d=N_d-N_{d+1}\quad(0\le d<H),\qquad c_H=N_H.         \tag{6.2}
\]
They satisfy
\[
                         \sum_{d=q}^Hc_d=N_q.            \tag{6.3}
\]

For every labelled fibre \(\alpha\) and class
\(\rho\in\mathscr R_{|\alpha|}\), introduce
\[
                         x_{\alpha,\rho}\in\{0,1\}.      \tag{6.4}
\]

### Level A: one resolution per fibre

\[
                    \sum_{\rho\in\mathscr R_{|\alpha|}}
                         x_{\alpha,\rho}=1
                    \qquad(\text{every }\alpha).         \tag{6.5}
\]

### Level B: global rank balance

\[
                  \sum_{\alpha,\rho}
                       n_{\rho,d}x_{\alpha,\rho}=c_d
                  \qquad(0\le d\le H).                  \tag{6.6}
\]

### Level C: forced pair-orbit balance

Let \(\mathfrak F_f\) be the fibres in (3.2).  Exact lower ownership at
every depth forces
\[
 \boxed{
 \sum_{\alpha\in\mathfrak F_f}
 \sum_{\rho\in\mathscr R_{m-2f}}
       n_{\rho,\ge q}x_{\alpha,\rho}=T_{f,q}}
 \qquad(f,q).                                          \tag{6.7}
\]
The upper equation is identical by complementation.

Summing (6.7) over \(f\) gives (6.3), so Level C refines Level B.

### Level D: labelled lower and upper ownership

The complete coefficient-one assignment is
\[
 \boxed{
 \sum_{\alpha,\rho}
       a^-_{\alpha,\rho,q}(T)x_{\alpha,\rho}=1}
 \quad
 \left(T\in\binom{[2m]}{m-q},\ 0\le q\le H\right),     \tag{6.8}
\]
\[
 \boxed{
 \sum_{\alpha,\rho}
       a^+_{\alpha,\rho,q}(U)x_{\alpha,\rho}=1}
 \quad
 \left(U\in\binom{[2m]}{m+q},\ 0\le q\le H\right).     \tag{6.9}
\]
Equations (6.8)--(6.9), together with (6.5) and local legality of every
class, are the exact rank-balanced resolution problem.  They express
simultaneously:

* an integral partition of all middle owners;
* the Boolean SCD radius quotas;
* one consecutive path hit for every lower target;
* one consecutive path hit for every upper target; and
* nesting of all depths through one radius label and one direction word.

## 7. Fixed-frame infeasibility and the exact discrepancy

For one fixed \(f\), the left side of (6.7) is nonincreasing in \(q\),
because the active sets \(\{r_\rho\ge q\}\) are nested.  It is also at
most
\[
                              V_f.                       \tag{7.1}
\]
But
\[
 \frac{T_{f,q+1}}{T_{f,q}}
   =\frac{m-2f-q}{2(f+q+1)},                            \tag{7.2}
\]
so the required sequence increases whenever
\[
                              m-4f-3q-2>0.              \tag{7.3}
\]
Already \(f=q=0\) is impossible for \(m>2\).

At one fixed depth, the unavoidable target deficit is
\[
                         D_{m,q}
                           =\sum_f(T_{f,q}-V_f)_+.       \tag{7.4}
\]
At Gaussian depth \(q=A\sqrt m+o(\sqrt m)\), this is
\[
                         D_{m,q}
                            =(\kappa_A+o(1))\binom{2m}m,
 \qquad \kappa_A>0.                                    \tag{7.5}
\]

Thus no choice of direction words, phases, or resolution classes inside
the fibres of one fixed coordinate pairing can solve (6.5)--(6.9).
The exact remaining integral problem for coefficient one is the
multi-frame version of the same system: enlarge the variables by a pair
frame index, retain one middle-owner equation, and replace
(6.7) by the full cross-frame incidences (6.8)--(6.9).  The orbit census
above supplies the complete fixed-frame columns of that larger assignment
matrix.

