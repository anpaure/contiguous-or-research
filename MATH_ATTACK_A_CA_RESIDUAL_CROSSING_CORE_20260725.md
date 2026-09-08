# Residual cyclic crossing packets and bounded-defect Hall cores

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
long-running computation is used.

## 0. Verdict

This note does **not** prove \((\mathrm{CA}_A)\).  It gives an exact
owner-level and wreath-level form of the missing residual Hall gate and
proves two structural facts which were not contained in the residual-vector
criterion.

1.  Besides the bounded-rank survival packets, there is a second, literal
    cyclic packet system.  For every child family \(\mathcal A\), its members
    are the canonical owners which cross from a parent capable of entering
    \(\mathcal A\) to a canonical child outside \(\mathcal A\).  The exact
    permitted number of surviving crossings is

    \[
      b_{q-1}(N(\mathcal A))-b_q(\mathcal A),
    \]

    with the floor and high-quota terms retained exactly.  Covering every
    one of these crossing packets, together with the survival packets, is
    equivalent to residual nested completion.  When exceptional owners must
    be whole wreath rows, the same statement is an exact packet hypergraph on
    the actual wreaths of one exact factor.

2.  In the fixed window every inclusion-minimal residual Hall obstruction
    has integer deficiency at most the bounded target capacity.  It is a
    connected positive-parent Johnson core, and every one of its children
    has strictly too little private parent mass.  Thus arbitrary cuts reduce
    to bounded-defect cores, though the cores themselves need not have
    bounded cardinality or bounded order.

The obstruction to importing the survival-packet rounding is sharp already
at depth one.  Unless the canonical depth-one load is itself balanced, every
deficit target produces an active Hall-crossing packet of size

\[
  m+O_A(1)
\]

on **distinct actual wreath rows**.  Hence bounded target capacities do not
bound the ranks of the Hall packets.  The verified fixed-order star collar
does not see these singleton target cuts: a singleton \((m-q)\)-set is a
star of order \(m-q\), not fixed order.

The precise surviving owner-level lemma is consequently a small common
cover theorem for this unbounded-rank directed crossing-packet system.  A
whole-row cover is a stronger literal absorber target, not a necessary form
of every residual completion.  Prime-equivariant balanced flag flow
guarantees that every displayed crossing capacity is nonnegative, but does
not supply either cover.

## 1. Canonical flags and exact quota notation

Put

\[
 n=2m+1,\qquad V_q=\binom{[n]}{m-q},\qquad
 W=\binom nm,
\]

and let \(F\) be one oriented exact wreath factor.  Its owner set is
\(V_0\): every middle set \(X\) belongs to a unique wreath row of \(F\).
Write

\[
 \Gamma_0(X)=X\supset\Gamma_1(X)\supset\cdots\supset\Gamma_K(X)
 \tag{1.1}
\]

for the canonical same-start cyclic flag in that row, and put

\[
 \ell_q(S)=\#\{X\in V_0:\Gamma_q(X)=S\}.
 \tag{1.2}
\]

Thus \(\sum_{S\in V_q}\ell_q(S)=W\) at every depth.

Let \(b=(b_q)_{q=0}^K\) be balanced integral quotas, with

\[
 b_0(X)=1,
 \qquad
 b_q(S)=c_q+\mathbf 1_{H_q}(S),
 \tag{1.3}
\]

where

\[
 c_q=\left\lfloor\frac{W}{|V_q|}\right\rfloor,
 \qquad
 |H_q|=\rho_q:=W-c_q|V_q|.
 \tag{1.4}
\]

At depth zero take \(c_0=1\) and \(H_0=\varnothing\).  No independent
rankwise feasibility is assumed below unless explicitly stated.

For an exceptional owner family \(E\subseteq V_0\), define

\[
 a_q^E(S)=\#\{X\in E:\Gamma_q(X)=S\},
 \qquad
 f_q^E=\ell_q-a_q^E,
 \tag{1.5}
\]

and the required residual load

\[
 r_q^E=b_q-f_q^E=b_q-\ell_q+a_q^E.
 \tag{1.6}
\]

At depth zero, \(r_0^E=\mathbf1_E\).  At every depth,

\[
 \sum_{S\in V_q}r_q^E(S)=|E|.
 \tag{1.7}
\]

## 2. The exact directed crossing-packet theorem

For \(S\in V_q\), let

\[
 \mathcal O_q(S)=\{X\in V_0:\Gamma_q(X)=S\}
 \tag{2.1}
\]

be its canonical owner set.  For \(\mathcal A\subseteq V_q\), let

\[
 N_q(\mathcal A)
 =\{R\in V_{q-1}:S\subset R\text{ for some }S\in\mathcal A\}
 \tag{2.2}
\]

be its upper Boolean neighborhood.  Define the canonical crossing-owner
set

\[
 \mathcal C_q(\mathcal A)
 =\{X:\Gamma_{q-1}(X)\in N_q(\mathcal A),\ 
          \Gamma_q(X)\notin\mathcal A\}.
 \tag{2.3}
\]

Finally define the exact balanced collar

\[
 \kappa_q^b(\mathcal A)
 =b_{q-1}(N_q(\mathcal A))-b_q(\mathcal A).
 \tag{2.4}
\]

Using (1.3), this is exactly

\[
\boxed{
 \kappa_q^b(\mathcal A)
 =c_{q-1}|N_q(\mathcal A)|-c_q|\mathcal A|
  +|H_{q-1}\cap N_q(\mathcal A)|-|H_q\cap\mathcal A|.}
 \tag{2.5}
\]

There is no asymptotic replacement of a floor in (2.5).

### Theorem 2.1 — exact owner-cover characterization

The frozen canonical flags outside \(E\) extend to one common integral
nested resolution with load vector \(b_q\) at every depth if and only if
the following two systems hold.

For every \(q\ge1\) and \(S\in V_q\),

\[
\boxed{
 |E\cap\mathcal O_q(S)|
 \ge \ell_q(S)-b_q(S).}
 \tag{S}
\]

For every \(q\ge1\) and \(\mathcal A\subseteq V_q\),

\[
\boxed{
 |E\cap\mathcal C_q(\mathcal A)|
 \ge |\mathcal C_q(\mathcal A)|-\kappa_q^b(\mathcal A).}
 \tag{H}
\]

A nonpositive right side is void.  A right side larger than its owner set
correctly certifies impossibility.

#### Proof

Condition \((S)\) is exactly nonnegativity of (1.6), since

\[
 r_q^E(S)
 =b_q(S)-\ell_q(S)+|E\cap\mathcal O_q(S)|.
 \tag{2.6}
\]

Now fix \(q,\mathcal A\).  Every owner whose depth-\(q\) child lies in
\(\mathcal A\) has its depth-\((q-1)\) parent in
\(N_q(\mathcal A)\).  Therefore

\[
 |\mathcal C_q(\mathcal A)|
 =\ell_{q-1}(N_q(\mathcal A))-\ell_q(\mathcal A),
 \tag{2.7}
\]

and, restricted to \(E\),

\[
 |E\cap\mathcal C_q(\mathcal A)|
 =a_{q-1}^E(N_q(\mathcal A))-a_q^E(\mathcal A).
 \tag{2.8}
\]

Subtracting the residual parent mass from the residual child mass and using
(2.7)--(2.8) gives the exact identity

\[
\boxed{
 r_q^E(\mathcal A)-r_{q-1}^E(N_q(\mathcal A))
 =|\mathcal C_q(\mathcal A)|
  -|E\cap\mathcal C_q(\mathcal A)|
  -\kappa_q^b(\mathcal A).}
 \tag{2.9}
\]

Thus \((H)\) is exactly every adjacent inclusion-Hall inequality.  Under
\((S)\), (1.7) gives equal nonnegative total mass at adjacent ranks.
Clone each parent and child according to its residual multiplicity and use
Hall's theorem.  Integral matchings exist at every adjacent pair.  At every
intermediate target, biject its incoming and outgoing copies; the common
multiplicity permits concatenation into \(|E|\) paths, one from each root
of \(E\).  This proves sufficiency.  Necessity follows from the same Hall
inequalities and (2.6).  \(\square\)

### Packet form

Condition \((S)\) says that at most \(b_q(S)\) members of
\(\mathcal O_q(S)\) may survive.  It is therefore equivalent to meeting
every \((b_q(S)+1)\)-subset of \(\mathcal O_q(S)\), the previously known
survival packets.

Condition \((H)\) says that at most \(\kappa_q^b(\mathcal A)\) members of
\(\mathcal C_q(\mathcal A)\) may survive.  If
\(0\le\kappa_q^b(\mathcal A)<|\mathcal C_q(\mathcal A)|\), it is equivalent
to meeting every

\[
 \boxed{\bigl(\kappa_q^b(\mathcal A)+1\bigr)\text{-subset of }
             \mathcal C_q(\mathcal A).}
 \tag{2.10}
\]

These are the **directed Hall-crossing packets**.  If the collar is
negative, no completion with quotas \(b\) exists even after releasing every
owner.  If it is at least the crossing-set size, there is no packet.

## 3. Literal projection to the wreath rows

Let \(\varpi(X)\in F\) be the unique wreath row containing the middle owner
\(X\).  Suppose exceptions must be whole rows:

\[
 E=E(\mathcal B):=\{X:\varpi(X)\in\mathcal B\},
 \qquad \mathcal B\subseteq F.
 \tag{3.1}
\]

For a row \(P\in F\), put

\[
 \omega_{P,q}(\mathcal A)
 =|\{X:\varpi(X)=P,\ X\in\mathcal C_q(\mathcal A)\}|.
 \tag{3.2}
\]

Then (H) becomes the literal cyclic inequality

\[
\boxed{
 \sum_{P\in\mathcal B}\omega_{P,q}(\mathcal A)
 \ge |\mathcal C_q(\mathcal A)|-\kappa_q^b(\mathcal A).}
 \tag{3.3}
\]

Equivalently, take every owner packet in (2.10), project its owner
occurrences to their wreath rows, and delete repetitions.  The selected row
family \(\mathcal B\) must hit every resulting hyperedge.  This projection
is lossless: a projected packet is missed precisely when all of its owner
occurrences survive in their actual rows.

For survival packets, a fixed proper cyclic interval occurs at most once in
one row, so their projected ranks remain at most

\[
 2+\max_{q\le K}c_q=O_A(1).
 \tag{3.4}
\]

The Hall-crossing packets have no analogous bounded-rank conclusion; see
Section 6.

## 4. Monotonicity and the role of a common balanced flag flow

### Proposition 4.1 — releasing more canonical paths never creates a Hall
### defect

Fix the quota vectors \(b_q\).  If \(E\subseteq E'\), then for every
\(q,\mathcal A\),

\[
 r_q^{E'}(\mathcal A)-r_{q-1}^{E'}(N_q(\mathcal A))
 \le
 r_q^E(\mathcal A)-r_{q-1}^E(N_q(\mathcal A)).
 \tag{4.1}
\]

Nonnegativity of all residual node loads is also monotone under enlarging
\(E\).

#### Proof

It is enough to add one owner \(X\).  Write

\[
 R=\Gamma_{q-1}(X),\qquad S=\Gamma_q(X)\subset R.
\]

The change in the left side of (4.1) is

\[
 \mathbf1_{\{S\in\mathcal A\}}
 -\mathbf1_{\{R\in N_q(\mathcal A)\}}.
 \tag{4.2}
\]

If the first indicator is one, so is the second; hence (4.2) is zero or
minus one.  Equation (2.6) shows that every node residual only increases.
\(\square\)

For a whole released row \(P\), the cut deficiency decreases exactly by
\(\omega_{P,q}(\mathcal A)\).  Thus the Hall closure is a monotone covering
problem on actual cyclic packets; there is no adverse cut created by adding
an absorber row.

Suppose now that \(b\) is itself the load vector of one common balanced
nested resolution.  Then

\[
 b_q(\mathcal A)\le b_{q-1}(N_q(\mathcal A)),
\]

so

\[
 \boxed{\kappa_q^b(\mathcal A)\ge0\quad\text{for every }q,\mathcal A.}
 \tag{4.3}
\]

In particular, on prime dimensions the verified equivariant balanced flag
flow supplies quotas satisfying (4.3), together with exact deletion-label
homomesy.  What it does **not** supply is a small common row cover of the
crossing packets (2.10).  Equation (4.3) removes only the impossible
negative-collar case.

## 5. Bounded-defect Hall cores

The next result applies to any one residual transition.  Let \(P\) and
\(V\) be adjacent Boolean ranks, let \(u:P\to\mathbb Z_{\ge0}\) be parent
mass and \(v:V\to\mathbb Z_{\ge0}\) child mass, with equal totals.  For
\(\mathcal A\subseteq V\), put

\[
 D(\mathcal A)=v(\mathcal A)-u(N(\mathcal A)).
 \tag{5.1}
\]

For \(S\in\mathcal A\), its private parent mass relative to \(\mathcal A\)
is

\[
 p_{\mathcal A}(S)
 =u\bigl(N(S)\setminus N(\mathcal A\setminus\{S\})\bigr).
 \tag{5.2}
\]

### Theorem 5.1 — exact peeling and core classification

If some Hall inequality fails, there is an inclusion-minimal family
\(\mathcal A\) with deficiency

\[
 d:=D(\mathcal A)>0
 \tag{5.3}
\]

such that:

1. \(v(S)>0\) for every \(S\in\mathcal A\);
2. for every \(S\in\mathcal A\),
   \[
    \boxed{p_{\mathcal A}(S)\le v(S)-d;}
    \tag{5.4}
   \]
3. the graph on \(\mathcal A\) joining two children when they lie in a
   common parent \(R\) with \(u(R)>0\) is connected;
4. the total parent mass on parents which contain at least two members of
   \(\mathcal A\) is at least
   \[
    \boxed{(|\mathcal A|-1)d.}
    \tag{5.5}
   \]

Consequently, if \(v(S)\le C\) at every child, then

\[
 \boxed{1\le d\le C.}
 \tag{5.6}
\]

More generally, starting from any violating family, repeatedly remove a
child \(S\) whenever

\[
 p_{\mathcal A}(S)\ge v(S).
 \tag{5.7}
\]

Every removal preserves a positive Hall deficiency, and the process ends
at a nonempty core satisfying \(p_{\mathcal A}(S)<v(S)\) for every member.

#### Proof

Choose \(\mathcal A\) inclusion-minimal with \(D(\mathcal A)>0\).  A
zero-mass child could be removed without decreasing the deficiency, proving
(1).  For \(S\in\mathcal A\), exact subtraction gives

\[
 D(\mathcal A)-D(\mathcal A\setminus\{S\})
 =v(S)-p_{\mathcal A}(S).
 \tag{5.8}
\]

Minimality gives \(D(\mathcal A\setminus\{S\})\le0\).  Combining this with
(5.3)--(5.8) proves (5.4), and also

\[
 d\le v(S)
\]

for every \(S\), proving (5.6).

If the positive-parent intersection graph had components
\(\mathcal A_1,\ldots,\mathcal A_t\), their positive-mass parent
neighborhoods would be disjoint.  Hence

\[
 D(\mathcal A)=\sum_iD(\mathcal A_i).
\]

Some component would violate Hall, contradicting minimality unless
\(t=1\).  This proves (3).

Let \(M_1\) be the parent mass on parents containing exactly one member of
\(\mathcal A\), and \(M_{\ge2}\) the remaining parent mass in
\(N(\mathcal A)\).  Summing (5.4) over \(S\) gives

\[
 M_1\le v(\mathcal A)-|\mathcal A|d.
 \tag{5.9}
\]

Since

\[
 M_1+M_{\ge2}=u(N(\mathcal A))=v(\mathcal A)-d,
\]

subtraction yields (5.5).

Finally, if (5.7) holds, (5.8) gives

\[
 D(\mathcal A\setminus\{S\})\ge D(\mathcal A)>0.
\]

Thus peeling cannot empty a violating family and terminates at the stated
core.  \(\square\)

In the fixed window, assume first that the survival constraints \((S)\)
hold, and take \(u=r_{q-1}^E\), \(v=r_q^E\).  Then

\[
 0\le r_q^E(S)\le b_q(S)\le1+\max_{s\le K}c_s=:C_A^*,
 \tag{5.10}
\]

every inclusion-minimal obstruction has deficiency in
\(\{1,\ldots,C_A^*\}\), uniformly in \(m\).  This does not bound the size
of its connected core.

### Supermodular uncrossing law

The deficiency function satisfies

\[
\boxed{
 D(\mathcal A)+D(\mathcal B)
 \le D(\mathcal A\cup\mathcal B)+D(\mathcal A\cap\mathcal B).}
 \tag{5.11}
\]

Indeed,

\[
 N(\mathcal A\cup\mathcal B)=N(\mathcal A)\cup N(\mathcal B),
 \qquad
 N(\mathcal A\cap\mathcal B)
 \subseteq N(\mathcal A)\cap N(\mathcal B),
\]

and parent mass is nonnegative.  Thus two crossing violations uncross to a
violating union or a violating intersection.  Equation (5.11) does not by
itself imply that all minimal cores form a laminar family; no such claim is
made.

## 6. The depth-one linear-rank obstruction is literal and exact

At depth one, \(b_0=\ell_0=1\).  Therefore (2.7) and (2.4) give, for every
\(\mathcal A\subseteq V_1\),

\[
 |\mathcal C_1(\mathcal A)|-\kappa_1^b(\mathcal A)
 =b_1(\mathcal A)-\ell_1(\mathcal A).
 \tag{6.1}
\]

In particular, for one target \(S\in V_1\), every positive canonical
deficit

\[
 d_S=b_1(S)-\ell_1(S)>0
 \tag{6.2}
\]

forces the exact row-cover condition

\[
\boxed{
 |E\cap\mathcal C_1(\{S\})|\ge d_S.}
 \tag{6.3}
\]

The set \(S\) has exactly \(m+2\) middle supersets.  Exactly
\(\ell_1(S)\) of their owners canonically delete to \(S\), so

\[
 |\mathcal C_1(\{S\})|=m+2-\ell_1(S),
 \qquad
 \kappa_1^b(\{S\})=m+2-b_1(S).
 \tag{6.4}
\]

Thus its crossing packets have size

\[
\boxed{m+3-b_1(S)=m+O(1).}
 \tag{6.5}
\]

### Lemma 6.1 — distinct-row property

For a fixed oriented wreath row, \(1\le q\le m-1\), and a fixed
\((m-q)\)-set \(S\), at most
one owner in that row belongs to \(\mathcal C_q(\{S\})\).  This holds for
every \(q\ge1\).

#### Proof

Put \(r=m-q\).  In one row the canonical parents are the cyclic intervals
\(I(j,r+1)\), and their canonical children are \(I(j,r)\).  Since
\(r+1\le m<n/2+1\), an \(r\)-set is contained in at most two cyclic
\((r+1)\)-intervals.  If it is contained in two, it is their common cyclic
\(r\)-interval.  Of the two extensions, exactly one has \(S\) as its
same-start canonical child; the other is a crossing owner.  If it is
contained in only one parent interval, that parent contributes at most one
crossing owner.  \(\square\)

By Lemma 6.1 every packet in (6.5) projects to the same number of **distinct
actual wreath rows**.  Consequently:

### Corollary 6.2 — bounded-capacity packet rounding stops at the Hall gate

If the canonical depth-one load is not balanced for the chosen quota
vector \(b_1\), then some deficit target has an active Hall-crossing packet
of rank at least

\[
 m+1.
 \tag{6.6}
\]

More generally, throughout a fixed window let

\[
 C_A=\max_{q\le K}c_q.
\]

For a singleton \(S\in V_q\),

\[
 \kappa_q^b(\{S\})
 \ge (m+q+1)-(C_A+1)=m+q-C_A.
 \tag{6.7}
\]

Hence every active singleton crossing packet has at least

\[
 m+q-C_A+1
 \tag{6.8}
\]

distinct wreath vertices.

#### Proof

If \(\ell_1\ne b_1\), their equal total masses imply a target with
\(b_1(S)>\ell_1(S)\).  Balanced depth-one quotas are one or two, so (6.5)
is at least \(m+1\); Lemma 6.1 preserves the rank on wreath projection.

For general \(q\), the singleton has \(m+q+1\) parents.  Every parent quota
is at least one and \(b_q(S)\le C_A+1\), giving (6.7).  If the packet is
active, its size is \(\kappa+1\), and Lemma 6.1 again makes its wreath rows
distinct.  \(\square\)

The survival packets have rank \(O_A(1)\); the Hall-crossing packets can
have rank \(\Theta(m)\) on the same literal factor.  Thus the deterministic
bounded-rank threshold rounding for survival packets cannot simply be
reused for the residual Hall system.

The verified fixed-order star collar does not contradict Corollary 6.2.
A singleton target \(S\in V_q\) is the containment star with prescribed set
\(T=S\), of order \(|T|=m-q\), whereas that theorem holds for each fixed
order \(t\).  Moreover, a crossing owner records the existence of **any**
sibling child in the target family, whereas one adjacent-swap graph exposes
only one selected sibling per owner.

## 7. Exact depth-one potential dual for compatibility cost

The preceding packet obstruction has an equivalent min-cost form which
shows why one-family Hall tests do not measure the full labelled cost.

Assume \(m\ge2\).  Let \(\phi(X)=\Gamma_1(X)\) be the canonical child of the middle owner
\(X\), and suppose \(b_1\) is a feasible depth-one quota vector.  Let
\(M(\phi,b_1)\) be the minimum number of owners for which
\(\psi(X)\ne\phi(X)\), over all maps

\[
 \psi(X)\subset X,\qquad |\psi(X)|=m-1,
 \qquad |\psi^{-1}(S)|=b_1(S).
 \tag{7.1}
\]

Put \(g(S)=b_1(S)-\ell_1(S)\).  For a nonnegative integral potential
\(z:V_1\to\mathbb Z_{\ge0}\), set

\[
 P_X(z)=
 \left(
  \max_{\substack{T\subset X,\ |T|=m-1\\T\ne\phi(X)}}z(T)
  -z(\phi(X))-1
 \right)_+.
 \tag{7.2}
\]

### Theorem 7.1 — exact integral potential formula

\[
\boxed{
 M(\phi,b_1)
 =\max_{\substack{z:V_1\to\mathbb Z_{\ge0}\\\min z=0}}
 \left\{
  \sum_{S\in V_1}g(S)z(S)-\sum_{X\in V_0}P_X(z)
 \right\}.}
 \tag{7.3}
\]

Equivalently, let

\[
 V_1=\mathcal A_0\supseteq\mathcal A_1\supseteq\cdots
 \supseteq\mathcal A_h\ne\varnothing
 \tag{7.4}
\]

be a finite nested sequence, with repetitions allowed, and put

\[
 \chi(\mathcal A_t,\mathcal A_{t-1})
 =\#\{X:\phi(X)\notin\mathcal A_{t-1},\ 
          \partial X\cap\mathcal A_t\ne\varnothing\},
 \tag{7.5}
\]

where \(\partial X\) is the family of \((m-1)\)-facets of \(X\).  Then

\[
\boxed{
 M(\phi,b_1)
 =\max_{(7.4)}
 \sum_{t=1}^h
 \bigl(g(\mathcal A_t)-
       \chi(\mathcal A_t,\mathcal A_{t-1})\bigr),}
 \tag{7.6}
\]

where the empty sequence contributes zero.

#### Proof

Use the transportation LP with variables \(x_{X,S}\) on
\(S\subset X\), parent supply one, child demand \(b_1(S)\), and cost zero
when \(S=\phi(X)\), one otherwise.  The inclusion matrix is a network
matrix, so the integral optimum equals the LP optimum.  Its dual is

\[
 \max\left\{
  \sum_X\alpha_X+\sum_Sb_1(S)z(S):
  \alpha_X+z(S)\le\mathbf1_{\{S\ne\phi(X)\}}
 \right\}.
 \tag{7.7}
\]

Integral costs and total unimodularity permit integral dual potentials.
Adding a constant to all \(z(S)\) and subtracting it from all \(\alpha_X\)
does not change the objective, because \(\sum_Sb_1(S)=|V_0|\).  Normalize
\(\min z=0\).  For fixed \(z\), the best parent potential is

\[
 \alpha_X
 =\min\left\{-z(\phi(X)),\ 
       1-\max_{T\subset X,\ T\ne\phi(X)}z(T)\right\}
 =-z(\phi(X))-P_X(z).
 \tag{7.8}
\]

Since \(\sum_Xz(\phi(X))=\sum_S\ell_1(S)z(S)\), substitution yields
(7.3).

For integral \(z\), let

\[
 \mathcal A_t=\{S:z(S)\ge t\},\qquad 1\le t\le\max z.
\]

Layer-cake summation gives

\[
 \sum_Sg(S)z(S)=\sum_tg(\mathcal A_t).
\]

The quantity \(P_X(z)\) counts exactly the integers \(t\) for which some
noncanonical facet of \(X\) belongs to \(\mathcal A_t\) while
\(\phi(X)\notin\mathcal A_{t-1}\).  Summing in \(X,t\) gives (7.5)--(7.6).
Conversely, if \(\mathcal A_1\ne V_1\), every nested sequence (7.4) is the
level-set sequence of
\(z(S)=|\{t:S\in\mathcal A_t\}|\), and this potential has minimum zero.
Any leading repetitions \(\mathcal A_1=\cdots=\mathcal A_j=V_1\) may be
deleted: each has \(g(V_1)=0\), and after deletion the first remaining
crossing penalty is still measured against \(\mathcal A_0=V_1\), hence is
zero.  Thus allowing such repetitions neither changes nor enlarges the
maximum.  \(\square\)

The height-one part of (7.6) is merely

\[
 \max_{\mathcal A}g(\mathcal A)
 =\sum_Sg(S)_+,
\]

the ordinary histogram deficit.  Additional nested levels are the exact
path-root correction cost caused by cyclic owner compatibility.  Thus
marginal balance, or even all isolated fixed-order star estimates, does not
control the required labelled support without a theorem bounding the
nested potential in (7.3).

## 8. Precise proved/conditional boundary

The following owner-level statement is now proved and is exact for the
residual gate.

> For one oriented exact factor and one common balanced quota flow, an owner
> family \(E\) supports an integral common nested completion if and only if
> it meets every survival packet and every directed Hall-crossing packet
> (2.10).  Every minimal residual obstruction is a connected Hall core of
> deficiency at most \(C_A^*\).

Under the additional literal-absorber restriction to whole rows, the owner
packets project losslessly and give the following stronger statement.

> For one oriented exact factor and one common balanced quota flow, a whole
> row family \(\mathcal B\) supports an integral common nested completion if
> and only if it hits every projected survival packet and every projected
> directed Hall-crossing packet (2.10).  Every minimal residual obstruction
> is a connected Hall core of deficiency at most \(C_A^*\).

What remains unproved at owner level is the quantitative cover assertion

> For every fixed \(A\), choose one exact factor, one common balanced quota
> flow, and an owner family
> \[
>  |E|=o_A(W/\sqrt m)
> \]
> which meets both packet systems through every controlled depth.

A stronger, fully row-packetized sufficient assertion is:

> For every fixed \(A\), choose one exact factor, one common balanced quota
> flow, and a row family
> \[
>  |\mathcal B|=o_A(\operatorname{Cat}_m/\sqrt m)
> \]
> which hits **both** packet systems through every depth
> \(q\le\lceil A\sqrt m\rceil\).

The bounded-rank rounding theorem proves the survival half once its
fractional cover has the required size.  Corollary 6.2 proves that it gives
no automatic rounding theorem for the Hall half: the latter already has
linear-rank packets at depth one.  The star collar excludes certain
fixed-order marginal cuts, and prime-equivariant flow makes every collar
nonnegative, but neither controls the high-order connected cores in
Theorem 5.1 or the nested potential (7.3).

## 9. Adversarial audit

1. **Fixed quotas in monotonicity.** Proposition 4.1 holds only while the
   quota vectors \(b_q\) are fixed.  Reselecting high-quota sets can change
   the collar and is not covered.
2. **All owners versus whole rows.** Theorem 2.1 is first proved for an
   arbitrary owner family.  Section 3 separately imposes literal wreath-row
   closure and projects every owner packet; no ownerwise selection is passed
   off as a cyclic absorber.
3. **Negative collars.** The packet description uses size \(\kappa+1\) only
   for \(\kappa\ge0\).  A negative collar is correctly declared impossible.
   Prime-equivariant common flow supplies nonnegative collars only on prime
   dimensions and is not claimed to prove the all-\(m\) theorem.
4. **Floor terms.** Formula (2.5) retains both floor baselines and both
   high-quota intersections.  No proportional replacement is used.
5. **Core defect versus core size.** Theorem 5.1 bounds only the integer
   deficiency, not the cardinality, order, or number of cores.
6. **Uncrossing scope.** Supermodularity yields the stated union/intersection
   alternative.  It does not prove a laminar description of all minimal
   obstructions.
7. **Linear packet rank.** The distinct-row statement uses the canonical
   same-start interval flags and \(q\ge1\), so the parent interval length is
   at most \(m\).  It does not apply to an arbitrary noncyclic nested owner
   system.
8. **Active depth-one packet.** Activity is proved whenever
   \(\ell_1\ne b_1\): equal total masses force a positive deficit.  If the
   canonical depth-one load is already balanced, no depth-one obstruction is
   asserted.
9. **Potential dual scope.** Theorem 7.1 is an exact one-transition theorem
   at depth one.  It is not promoted to a simultaneous all-depth row-cost
   formula.
10. **Constant one.** No fixed-window alignment or constant-one conclusion
    is claimed.  The unbounded-rank common crossing cover remains open.
