# Inner-flag coherence: the fixed central rotor projection and a monotone-cycle obstruction

Date: 2026-07-26

Method: pure mathematics only.  This note strengthens the one-baseline
flag-coherent reduction.  It does not assume an unproved matching theorem.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}.
\]

Choose

\[
 q_0\longrightarrow\infty,\qquad q_0=o(m^{1/3}),
 \qquad H/\sqrt m\longrightarrow\infty,\qquad H=o(m),
\tag{0.1}
\]

and let \(\mathcal D\) be one full symmetric-chain decomposition of
\(B_{2m}\).  Retain the \(N_{q_0}\) chains

\[
 \Omega=\mathcal D_{\ge q_0}.
\tag{0.2}
\]

The already established flag-coherent reduction says that an
inner-flag-coherent radius-\(H\) bridge-one path cover of \(\Omega\) with

\[
 p=o(W/H)
\tag{0.3}
\]

would prove coefficient one.  The purpose of this note is to determine
exactly what the annular collars can and cannot do to that gate.

There are three conclusions.

1. **Outer collars cannot create central chronology.**  Every bridge-one
   edge between two inner-flag-coherent extensions projects to a genuine
   radius-\(q_0\) rotor edge between their original SCD flags.  Thus every
   admissible full path forest projects, with the same vertices, arcs, and
   number of paths, into one fixed directed graph
   \(\mathfrak R_{q_0}(\mathcal D)\).  In particular, no choice of outer
   collars can improve the central path-cover deficiency.

2. The ordered central flag words have an exact de Bruijn-type imbalance
   cut.  If \(A_u\) and \(B_u\) count chains whose central word has prefix,
   respectively suffix, \(u\) of length \(2q_0-1\), then every projected
   path cover satisfies

   \[
    \boxed{
    p\ge {1\over2}\sum_u|A_u-B_u|.}
   \tag{0.4}
   \]

   A cycle factor on all but \(r\) states requires the stronger necessary
   inequality

   \[
    \boxed{
    r\ge {1\over2}\sum_u|A_u-B_u|.}
   \tag{0.5}
   \]

   These are statewise conditions on the chosen SCD; scalar owner and
   target equations do not see them.

3. If every clipped central word is monotone in one common coordinate
   order, then

   \[
    \boxed{
    {1\over2}\sum_u|A_u-B_u|
       \ge {N_{q_0}\over n-2q_0+1}.}
   \tag{0.6}
   \]

   The Greene--Kleitman/BTK SCD, and every coordinate relabeling of it,
   has this monotonicity.  Consequently no inner-flag-coherent cyclic
   packet factor can cover all but fewer than

   \[
          {N_{q_0}\over n-2q_0+1}=(1+o(1)){W\over2m}
   \tag{0.7}
   \]

   retained BTK chains.  In particular, the floor-corrected leave
   \(r<2m\) in the proposed length-\(2m\) cycle factor is impossible for
   BTK.

The last lower bound does **not** refute the path-forest compiler: under
\(H=o(m)\),

\[
 {W/m\over W/H}={H\over m}=o(1).
\tag{0.8}
\]

Thus inner-flag coherence is compatible with the required *path* scale,
but it is incompatible with near-complete *cycles* in every monotone SCD.
The surviving construction must either use a nonmonotone SCD or exploit
open paths with their necessary boundary imbalance.

## 1. The forced central states

Let \(C\in\Omega\) have native radius \(d\ge q_0\), written

\[
 C_{-d}\subset\cdots\subset C_{d},
 \qquad |C_i|=m+i.
\tag{1.1}
\]

Its forced radius-\(q\) truncation, for \(q\le d\), is

\[
 \tau_q C=(A_C^{(q)};
   w_1^{(q)}(C),\ldots,w_{2q}^{(q)}(C);B_C^{(q)}),
\tag{1.2}
\]

where

\[
 A_C^{(q)}=C_{-q},\qquad B_C^{(q)}=[n]\setminus C_q,
\tag{1.3}
\]

and the ordered labels are determined by

\[
 C_{-q+i}=C_{-q}+\{w_1^{(q)}(C),\ldots,w_i^{(q)}(C)\}
 \qquad(0\le i\le2q).
\tag{1.4}
\]

All entries of the word

\[
                         w^{(q)}(C)
 =(w_1^{(q)}(C),\ldots,w_{2q}^{(q)}(C))
\tag{1.5}
\]

are distinct.  At \(q=q_0\), every object in (1.2)--(1.5) is fixed by
the original SCD.  Reassigning the middle corner or reordering either
inner port would destroy shallow flag coherence.

Define the **central rotor graph** \(\mathfrak R_q(\mathcal D)\) on
\(\mathcal D_{\ge q}\) by putting \(C\to C'\) precisely when there are

\[
 x\in A_C^{(q)},\qquad y\in B_C^{(q)}
\]

such that

\[
 \begin{aligned}
 A_{C'}^{(q)}&=A_C^{(q)}-x+y,\\
 w^{(q)}(C')&=(x,w_1^{(q)}(C),\ldots,w_{2q-1}^{(q)}(C)),\\
 B_{C'}^{(q)}&=B_C^{(q)}-y+w_{2q}^{(q)}(C).
 \end{aligned}
\tag{1.6}
\]

This is not a relaxation: (1.6) is exactly the genuine radius-\(q\)
rotor formula on the two forced SCD states.

## 2. Extension-independent projection

A complete radius-\(H\) state has the form

\[
 \omega=(L;z_1,\ldots,z_{2H};R).
\tag{2.1}
\]

Absorbing the first and last \(H-q\) collar coordinates gives

\[
 \tau_q\omega=
 \bigl(L+\{z_1,\ldots,z_{H-q}\};
 z_{H-q+1},\ldots,z_{H+q};
 R+\{z_{H+q+1},\ldots,z_{2H}\}\bigr).
\tag{2.2}
\]

### Theorem 2.1 (central projection obstruction)

Give every \(C\in\Omega\) any radius-\(H\) extension which preserves its
SCD flag through its native radius.  Let \(C\ne C'\).  If their complete
states are joined by a bridge-one edge, then

\[
                    C\longrightarrow C'
       \quad\hbox{in }\mathfrak R_{q_0}(\mathcal D).
\tag{2.3}
\]

Consequently, if the complete states have a spanning bridge-one directed
linear forest with \(p\) components, then

\[
 \mathfrak R_{q_0}(\mathcal D)
 \quad\hbox{contains a spanning directed linear forest with }p
 \hbox{ components}.                                         \tag{2.4}
\]

#### Proof

The bridge-one classification consists of identity, genuine full rotor,
and promotion.

A full rotor becomes a radius-\(q_0\) rotor after (2.2).  For a promotion
which removes slot \(j\), direct substitution in (2.2) gives three
possibilities:

\[
 \begin{array}{c|c}
 j\le H-q_0&\text{identity after projection},\\
 H-q_0<j\le H+q_0&\text{radius-\(q_0\) promotion},\\
 j>H+q_0&\text{radius-\(q_0\) rotor}.
 \end{array}
\tag{2.5}
\]

The projected identity cannot join two distinct SCD chains.  A
radius-\(q_0\) promotion preserves the rank-\((m+q_0)\) top mask.  The
two projected states are members of distinct SCD chains, and an SCD
partitions that rank, so they cannot have the same top mask.  Hence the
first two cases in (2.5) are impossible.  The only remaining projected
edge is a genuine rotor, which is exactly (1.6).

Projection does not change the chain vertices or the incidence of the
selected forest.  Thus all its arcs survive as arcs of
\(\mathfrak R_{q_0}(\mathcal D)\), proving (2.4). \(\square\)

Define

\[
 \operatorname{cpath}_{q_0}(\mathcal D)
 =N_{q_0}-\max\{|E(F)|:F\subseteq\mathfrak R_{q_0}(\mathcal D)
                    \text{ is a directed linear forest}\}.
\tag{2.6}
\]

If \(\operatorname{fcpath}_{q_0,H}(\mathcal D)\) denotes the optimized
full inner-flag-coherent bridge path number, Theorem 2.1 gives the exact
extension-independent inequality

\[
 \boxed{
 \operatorname{fcpath}_{q_0,H}(\mathcal D)
 \ge \operatorname{cpath}_{q_0}(\mathcal D).}
\tag{2.7}
\]

Thus a necessary condition for the one-baseline theorem is

\[
 \operatorname{cpath}_{q_0}(\mathcal D)=o(W/H).
\tag{2.8}
\]

## 3. The exact ordered-word imbalance

For an ordered \((2q-1)\)-tuple \(u\) of distinct coordinates, put

\[
 A_u^{(q)}
 =\#\{C\in\mathcal D_{\ge q}:
       (w_1^{(q)}(C),\ldots,w_{2q-1}^{(q)}(C))=u\},
\tag{3.1}
\]

\[
 B_u^{(q)}
 =\#\{C\in\mathcal D_{\ge q}:
       (w_2^{(q)}(C),\ldots,w_{2q}^{(q)}(C))=u\}.
\tag{3.2}
\]

Both histograms have total mass \(N_q\).  Define their total-variation
imbalance

\[
 \Delta_q(\mathcal D)
 ={1\over2}\sum_u|A_u^{(q)}-B_u^{(q)}|.
\tag{3.3}
\]

### Theorem 3.1 (de Bruijn boundary cut)

Every directed linear forest on all \(N_q\) vertices of
\(\mathfrak R_q(\mathcal D)\), with \(p\) components, satisfies

\[
                         \boxed{p\ge\Delta_q(\mathcal D).}
\tag{3.4}
\]

If \(\mathfrak R_q(\mathcal D)\) has a directed cycle factor on all but
\(r\) vertices, then

\[
                         \boxed{r\ge\Delta_q(\mathcal D).}
\tag{3.5}
\]

#### Proof

For a rotor edge \(C\to C'\), the word equation in (1.6) gives

\[
 (w_2^{(q)}(C'),\ldots,w_{2q}^{(q)}(C'))
 =(w_1^{(q)}(C),\ldots,w_{2q-1}^{(q)}(C)).
\tag{3.6}
\]

Thus an edge of type \(u\) uses one source counted by \(A_u^{(q)}\) and
one target counted by \(B_u^{(q)}\).  A directed linear forest has
outdegree and indegree at most one, so the number of selected edges of
type \(u\) is at most

\[
                         \min(A_u^{(q)},B_u^{(q)}).
\]

Summing over \(u\), a forest with \(N_q-p\) edges satisfies

\[
 N_q-p\le\sum_u\min(A_u^{(q)},B_u^{(q)})
 =N_q-\Delta_q(\mathcal D),
\]

which proves (3.4).

On the vertex set of a cycle factor, every prefix occurrence is paired
with exactly one suffix occurrence of the same type, so its restricted
histograms agree.  Removing one vertex changes each histogram in one unit
and hence can decrease their total \(\ell_1\)-difference by at most two.
Therefore removing \(r\) vertices can repair total variation at most
\(r\), proving (3.5). \(\square\)

Combining Theorems 2.1 and 3.1 gives the promised collar-independent
necessary condition

\[
 \boxed{
 p\ge\Delta_{q_0}(\mathcal D).}
\tag{3.7}
\]

There is also an all-threshold version.  In a \(p\)-path cover of
\(\Omega\), mark the \(N_q\) chains of native radius at least \(q\).  The
number of marked--marked path edges is at least

\[
                         2N_q-N_{q_0}-p.
\tag{3.8}
\]

Every such edge projects to a radius-\(q\) rotor.  The proof above bounds
the number of these edges by \(N_q-\Delta_q(\mathcal D)\).  Hence,
simultaneously for every \(q_0\le q\le H\),

\[
 \boxed{
 \Delta_q(\mathcal D)\le N_{q_0}-N_q+p.}
\tag{3.9}
\]

At \(q=q_0\), this reduces exactly to (3.7).

## 4. Monotone central words and the BTK cycle no-go

Assume that there is a total order \(\ell:[n]\to[n]\) such that, for
every \(C\in\mathcal D_{\ge q}\),

\[
 \ell(w_1^{(q)}(C))<\ell(w_2^{(q)}(C))<\cdots
 <\ell(w_{2q}^{(q)}(C)).
\tag{4.1}
\]

### Theorem 4.1 (monotone boundary imbalance)

Under (4.1),

\[
 \boxed{
 \Delta_q(\mathcal D)\ge{N_q\over n-2q+1}.}
\tag{4.2}
\]

#### Proof

Put \(k=2q-1\), and for an ordered \(k\)-tuple \(u\) define

\[
                         f(u)=\sum_{x\in u}\ell(x).
\tag{4.3}
\]

Then

\[
 \begin{aligned}
 \sum_u f(u)(A_u^{(q)}-B_u^{(q)})
 &=\sum_{C\in\mathcal D_{\ge q}}
   \bigl(\ell(w_1^{(q)}(C))-\ell(w_{2q}^{(q)}(C))\bigr).
 \end{aligned}
\tag{4.4}
\]

The absolute value of every summand is at least \(2q-1=k\), by strict
monotonicity.  Thus the absolute value of (4.4) is at least \(kN_q\).

The minimum sum of \(k\) distinct labels is \(k(k+1)/2\), and the
maximum is \(k(2n-k+1)/2\).  Hence the range of \(f\) is

\[
                         k(n-k).
\tag{4.5}
\]

The signed measure \(A^{(q)}-B^{(q)}\) has total mass zero.  Therefore

\[
 \left|\sum_u f(u)(A_u^{(q)}-B_u^{(q)})\right|
 \le k(n-k)\Delta_q(\mathcal D).
\tag{4.6}
\]

Combining (4.4)--(4.6), and using \(n-k=n-2q+1\), proves (4.2).
\(\square\)

### Corollary 4.2 (BTK cyclic-packet obstruction)

For the Greene--Kleitman/BTK SCD, and every coordinate relabeling of it,

\[
 \Delta_q(\mathcal D_{\rm BTK})
 \ge{N_q\over n-2q+1}.                                      \tag{4.7}
\]

Consequently every inner-flag-coherent bridge path cover of
\(\mathcal D_{{\rm BTK},\ge q_0}\) has at least the number of paths in
(0.7), and every bridge cycle factor omits at least that many states.

#### Proof

Encode a BTK chain by its standard ballot word.  Its free coordinates are
the persistent unmatched positions

\[
                         z_1<z_2<\cdots<z_{2d}.
\]

Clipping a native-radius-\(d\) chain to radius \(q\le d\) gives the
central word

\[
                         z_{d-q+1},\ldots,z_{d+q},
\]

which is strictly increasing in the ambient coordinate order.  A
coordinate relabeling merely transports this common total order.  Apply
Theorems 2.1, 3.1, and 4.1. \(\square\)

If \(q_0=o(\sqrt m)\), then \(N_{q_0}=(1-o(1))W\), so (4.7) is
\((1+o(1))W/(2m)\).  This is exponentially larger than the divisibility
leave \(r<2m\), proving the claimed cycle no-go.  On the other hand, for
the scale (0.1),

\[
 {N_{q_0}/(n-2q_0+1)\over W/H}
 =(1+o(1)){H\over2m}=o(1),
\tag{4.8}
\]

so the same theorem leaves the open-path compiler quantitatively alive.

## 5. Exact boundary

Proved here:

1. every annular bridge between inner-flag-coherent states projects to a
   fixed central SCD rotor edge;
2. collar choices cannot reduce the central path-cover deficiency;
3. the exact prefix/suffix imbalance cuts (3.4), (3.5), and (3.9);
4. the monotone-word lower bound (4.2); and
5. the resulting impossibility of a floor-leave cyclic packet factor in
   every BTK or permuted-BTK scaffold.

Not proved here:

1. a nonmonotone SCD with
   \(\Delta_{q_0}=o(W/H)\);
2. a spanning central rotor path forest with \(o(W/H)\) components even
   when the imbalance cut passes;
3. a simultaneous lift of such a central forest through every protected
   annular depth; or
4. coefficient one.

Together with the one-baseline flag-coherent reduction, the correct
conclusion is:

\[
 \boxed{
 \begin{gathered}
 \text{shallow SCD coherence removes the second baseline, but it freezes}\
 \text{a central de Bruijn rotor graph before any annular collar is chosen;}\
 \text{BTK cannot support near-complete cycles, while a nonmonotone}\
 \text{low-boundary open-path SCD remains a live exact target.}
 \end{gathered}}
\]

