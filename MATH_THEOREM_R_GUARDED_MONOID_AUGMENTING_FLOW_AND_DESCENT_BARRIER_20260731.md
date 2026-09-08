# Guarded monoid repair: exact augmenting-flow theorem, descent barrier, and regenerative consequence

Date: 2026-07-31  
Lane: R, pure mathematics  
Status: an unconditional positive theorem under an explicit serializable
unit-debt/gammoid hypothesis; a sharp counterexample to atomic or
bounded-radius strict descent; a conditional \(B(k)+O(1)\) implication.
No \(K17\) word or unconditional all-\(k\) bound is claimed.

## 0. Verdict

The exact finite run monoid and truncated shadow monoid do two important
things:

1. they give a finite, exact signature for the replay and upper-provider
   effect of every signed-fragment switch; and
2. they make a proposed compound repair and its protected witnesses
   mechanically checkable.

They do **not** imply that some bounded marked-preserving switch strictly
decreases replay/upper deficiency.  This fails in the smallest nontrivial
two-toggle union-monoid example: both elementary switches are uphill, while
their compound is perfect.  For every fixed radius \(r\), an
\((r+1)\)-toggle version makes every compound of support at most \(r\)
uphill.  Thus neither finiteness, exact owner preservation, disjoint switch
supports, nor a complete bounded-radius catalogue supplies a local
Lyapunov theorem.

There are two correct replacements.

* On the complete exact guarded state graph, repair with height barrier
  \(h\) is equivalent to reachability inside the \(h\)-sublevel set.
  Failure gives the reachable sublevel set as a literal cut certificate.
  The exact cost-to-go, not raw deficiency, is a contracting potential.
* If the guarded catalogue has a **serializable unit-debt network** (or,
  more generally, a gammoid of closed repair packets), integral
  max-flow/min-cost flow (respectively Rado's matroidal Hall theorem) gives
  a genuine repair-or-cut dichotomy.  Completed paths strictly decrease
  the weighted terminal defect; individual arcs may be neutral or uphill.

This yields the exact additive-constant implication.  If the post-guard
network has uniformly bounded **literal-weighted** leave (including any
terminal middle-owner leave), uniformly bounded physical/cap cost, complete
deep-shadow guards, and regenerates the same bounded sidecar state, then

\[
                         \nu(k)\le B(k)+O(1).
\]

Constant packet-count leave alone is insufficient: one unresolved run
packet can represent \(\Theta(\sqrt k)\) literal masks.  Exact CLMT/middle
ownership is needed for equality, but not for an additive constant: a
bounded family of terminal middle masks may be appended literally.  Any
central or palette debt required by the next Pascal step is carried debt,
not terminal debt, and must still be reset or contracted.

## 1. Exact monoid state

Fix a marked-preserving factor state \(x\).  A state contains the chosen
owner incidences, its physical fragment order and orientations, the marked
bank, and every occurrence label needed to distinguish equal masks.

### 1.1 Run monoid

For one coordinate trace and a replay depth \(D\), retain:

* whether the trace is all one;
* its first and last bit;
* the leading and trailing positive-run lengths capped at \(D+1\); and
* the occurrence-labelled internal positive runs of length at most \(D\).

Concatenation merges the two boundary runs exactly when both boundary bits
are one.  This gives an associative finite weighted monoid
\(\mathcal R_{D+1}\).  Reversal exchanges its two boundary states and
preserves its internal-run multiset.  Taking the product over coordinates
is still finite for each fixed dimension and computes the exact replay
derivative at every changed seam.

The phrase finite-state is not a uniform cardinality assertion:
\(\mathcal R_{D+1}\) grows with \(D\), and \(D=d(k)\) may grow with \(k\).

### 1.2 Truncated shadow monoid

For a nonempty set word \(V\) and a truncation rank \(h\), put

\[
 \mathcal U_h(V)=
 \bigl(u(V),P_h(V),S_h(V),I_h(V)\bigr),
\]

where \(u(V)\) is the total union and \(P_h,S_h,I_h\) are the multisets of
prefix, suffix, and interval unions of rank at most \(h\).  If \(*\) is
union convolution with ranks above \(h\) discarded, then

\[
\begin{aligned}
u(UV)&=u(U)\cup u(V),\\
P_h(UV)&=P_h(U)\uplus\bigl(u(U)*P_h(V)\bigr),\\
S_h(UV)&=S_h(V)\uplus\bigl(S_h(U)*u(V)\bigr),\\
I_h(UV)&=I_h(U)\uplus I_h(V)
              \uplus\bigl(S_h(U)*P_h(V)\bigr).
\end{aligned}                                                    \tag{1.1}
\]

This is the exact associative truncated-shadow monoid.  Multiplicities are
essential: a protected target of current load \(\mu\) may lose at most
\(\mu-1\) occurrences under the entire selected batch.

Put

\[
             \Sigma_{D,h}(V)=
             \mathcal R_{D+1}(V)\times\mathcal U_h(V).          \tag{1.2}
\]

For a signed-fragment switch, the old and new products in (1.2) give its
exact run and truncated-provider derivative.  The monoid records effects;
it does not assert that independently attractive derivatives can be
simultaneously installed.

### 1.3 Defect packets and literal weight

Let \(\mathcal O(x)\) be a declared occurrence-labelled packetization of:

* replay failures;
* missing upper targets of ranks at most \(h\); and
* any cap/socket debt which must be repaired inside the same physical word.

For \(o\in\mathcal O(x)\), let \(w(o)\) be an upper bound on the number of
distinct literal target masks which must be appended if \(o\) is left
unresolved.  Define the terminal-weight potential

\[
                   \Phi_w(x)=\sum_{o\in\mathcal O(x)}w(o).      \tag{1.3}
\]

When every token is one literal target, this specializes to ordinary
replay/upper deficiency.  A run packet need not have weight one.

Every target above \(h\) must either be included by increasing \(h\), or
have an explicit protected witness wholly outside all selected supports.
Current completeness above \(h\) is not such a batch guard.

## 2. Strict atomic descent is false

### Theorem 2.1 (two-toggle exact barrier)

There is a marked degree-preserving exchange system with:

* two disjoint elementary alternating \(C_4\) switches;
* the one-element clean run monoid;
* an exact finite Boolean-union shadow monoid; and
* four target labels,

such that the initial state has deficiency one, either elementary switch
raises the deficiency to two, and applying both gives deficiency zero.

#### Proof

Let

\[
                  G=K^A_{2,2}\ \dot\cup\ K^B_{2,2}.
\]

A feasible state chooses one perfect matching in each block.  Write
\(0\) for the direct and \(1\) for the cross matching.  Mark all left and
right resource vertices.  Each block's alternating \(C_4\) toggle preserves
every degree and every marked resource.  A fixed marked path may be adjoined
disjointly without changing the example.

Take \(\mathcal R=\{1\}\) and the shadow-support monoid

\[
                    \mathcal S=(2^T,\cup,\varnothing),
             \qquad T=\{a,b,c,d\}.
\]

Label the two selected edges in each matching as follows:

\[
\begin{array}{c|c}
\text{matching}&\text{two edge labels}\\ \hline
A_0&c,d\\
A_1&a,b\\
B_0&a,\varnothing\\
B_1&c,d .
\end{array}
\]

The shadow label of a state is the union of its four selected edge labels.
Therefore

\[
\begin{array}{c|c|c}
\text{state}&\text{covered targets}&\Phi\\ \hline
00&\{a,c,d\}&1\\
10&\{a,b\}&2\\
01&\{c,d\}&2\\
11&\{a,b,c,d\}&0 .
\end{array}                                                    \tag{2.1}
\]

Both outgoing elementary switches from \(00\) are strictly uphill, but
their compound reaches \(11\).  Replay is clean in all four states.
\(\square\)

The Boolean-union monoid in this theorem is exactly the support quotient of
the truncated provider monoid: it forgets positive multiplicities and keeps
which formal targets have a provider.  Consequently no descent theorem
deduced only from finiteness, associativity, and marked degree preservation
can be valid.  The example is not asserted to be a literal PBBS subfactor;
additional PBBS geometry could still imply expansion and must be proved.

### Proposition 2.2 (minimality in the two-toggle union class)

Four targets are minimal for Theorem 2.1 among unweighted Boolean-union
models with two independent binary toggles, initial deficiency one, both
single-toggle deficiencies at least two, and perfect double-toggle state.

#### Proof

Write \(A_i,B_j\) for the target sets contributed by the two block
matchings.  If \(|T|\le3\), deficiency at least two at the two single-toggle
states gives

\[
 |A_1\cup B_0|\le1,\qquad |A_0\cup B_1|\le1.
\]

Hence \(|A_1|\le1\), \(|B_1|\le1\), and
\(|A_1\cup B_1|\le2\), contrary to perfect coverage of a three-target
universe.  For smaller universes the same inequalities are stronger.
The construction (2.1) uses four targets.  \(\square\)

### Theorem 2.3 (no fixed-radius descent theorem)

For every \(r\ge1\) there is an exact finite clean-run/union-shadow system
with \(r+1\) independent \(C_4\) toggles such that:

* the all-zero state has deficiency one;
* every nonzero proper state has deficiency two; and
* the all-one state has deficiency zero.

Thus a catalogue containing every compatible compound of support at most
\(r\) has no descending move from the all-zero state.

#### Proof

Let the state be \(z\in\{0,1\}^{r+1}\).  Introduce a target \(\alpha\)
which block \(i\) provides exactly when \(z_i=1\); hence \(\alpha\) is
absent exactly at \(0\).  For every nonzero proper state
\(s\ne\mathbf1\), introduce two targets
\(\beta_s^1,\beta_s^2\).  Block \(i\) provides each of them exactly when
\(z_i\ne s_i\).  Such fixed edge labels are obtained by putting the target
on matching \(0\) when \(s_i=1\), and on matching \(1\) when \(s_i=0\).
Thus \(\beta_s^1,\beta_s^2\) are absent exactly at \(z=s\).

At \(0\), only \(\alpha\) is absent.  At a nonzero proper state \(s\),
only its two beta targets are absent.  At \(\mathbf1\), every target is
present.  A move supported on at most \(r\) blocks cannot take \(0\) to
\(\mathbf1\), so every such nonempty move is uphill.  \(\square\)

This closes every proposed theorem of the form “some bounded-support
catalogue switch strictly contracts raw deficiency.”  A global compound,
an allowed barrier, or an expansion hypothesis is indispensable.

## 3. Raw same-colour columns are not repair packets

The preceding example has individually legal \(C_4\) switches.  There is a
second, literal Johnson obstruction before one even reaches that stage.

### Proposition 3.1 (literal balance closure in \(J(7,3)\))

Let

\[
\begin{array}{lll}
A=123,&B=124,&C=134,\\
X=125,&Y=146,&Z=137.
\end{array}
\]

Consider the same-lower-colour exchange columns

\[
\begin{array}{lll}
e_1:\ AX\mapsto BX,& A\cap X=B\cap X=12,\\
e_2:\ BY\mapsto CY,& B\cap Y=C\cap Y=14,\\
e_3:\ CZ\mapsto AZ,& C\cap Z=A\cap Z=13.
\end{array}                                                   \tag{3.1}
\]

A \(0\)-\(1\) subset of these columns is owner-degree balanced if and only
if it is empty or contains all three.

#### Proof

The owner divergences are

\[
              \partial e_1=-A+B,\quad
              \partial e_2=-B+C,\quad
              \partial e_3=-C+A.
\]

For coefficients \(x_i\in\{0,1\}\), the coefficients at \(A,B,C\) are
\(-x_1+x_3,x_1-x_2,x_2-x_3\).  They vanish exactly when
\(x_1=x_2=x_3\).  The three together form the alternating
\(6\)-cycle

\[
                       A-X-B-Y-C-Z-A.                         \tag{3.2}
\]
\(\square\)

Consequently ordinary Hall support on the raw columns \(e_1,e_2\) may pass
while no nonempty factor-feasible repair exists if a guard forbids \(e_3\).
Atomic columns must first be closed into factor-feasible circuits or
serializable paths.  The balance equations are not hereditary and hence do
not themselves define a matroid.

## 4. The unconditional global potential-or-cut theorem

Let \(\Gamma\) be the finite directed graph of **exact guarded physical
states**.  An arc is present only when literal replay confirms its
marked-owner, topology, run, shadow, deep-witness, and cap transition.
Let \(F\) be the accepting states and let
\(\Phi:\Gamma\to\mathbb Z_{\ge0}\) be any exact physical deficiency.

For \(x\in\Gamma\) and \(h\ge0\), let

\[
 \Gamma_h(x)=
 \Gamma\bigl[\{v:\Phi(v)\le\Phi(x)+h\}\bigr],
\]

and let \(R_h(x)\) be the vertices reachable from \(x\) in
\(\Gamma_h(x)\).

### Theorem 4.1 (sharp barrier cut)

There is a guarded repair path from \(x\) to \(F\) whose deficiency never
exceeds \(\Phi(x)+h\) if and only if

\[
                         R_h(x)\cap F\ne\varnothing.           \tag{4.1}
\]

If the intersection is empty, \(R_h(x)\), together with its outgoing
boundary arcs, is an exact checkable obstruction.  The minimum necessary
barrier is

\[
             \beta(x)=\min\{h:R_h(x)\cap F\ne\varnothing\}.    \tag{4.2}
\]

#### Proof

A path with the stated barrier lies in \(\Gamma_h(x)\), so its endpoint is
in \(R_h(x)\cap F\).  Conversely the definition of reachability supplies
such a path whenever the intersection is nonempty.  If it is empty, every
path from \(x\) to \(F\) must cross the displayed sublevel boundary.
\(\square\)

In Theorem 2.1, \(R_0(00)=\{00\}\) and \(\beta(00)=1\).

For nonnegative physical arc costs, let

\[
        J(v)=\min\{\text{cost of a directed }v\text{-to-}F
                    \text{ path}\}.
\]

If \(J(v)<\infty\), a Bellman-optimal first arc does not increase \(J\);
tie it by the minimum remaining number of arcs among \(J\)-optimal paths.
The pair

\[
                         (J,\ell)                              \tag{4.3}
\]

strictly decreases lexicographically along a chosen optimal arc.  If
\(J(v)=\infty\), the full reachable set from \(v\) is forward-closed and
disjoint from \(F\).  Thus a contracting potential always exists after
solving global reachability; raw replay/upper deficiency need not be it.

## 5. Guarded unit-debt augmenting flow

The complete state graph is exact but enormous.  The following hypothesis
is the weakest ordinary-flow structure used here.

### Definition 5.1 (serializable unit-debt atlas)

A marked-preserving exchange atlas is serializable unit-debt when it admits
a directed integral-capacity network \(N\), with unit packet supply, having:

1. a super-source \(s\), and one capacity-one arc
   \(s\to s_o\) for every occurrence-labelled defect packet \(o\);
2. absorber vertices connected to a terminal \(t\);
3. resource vertices for every incidence, provider-withdrawal ticket,
   seam halo, protected occurrence, and cap socket which cannot be shared;
   every such vertex is split into an in/out pair joined by its declared
   integral capacity;
4. arcs labelled by exact \(\Sigma_{D,h}\) transitions;
5. along each transition, the live packet is either transported to one
   successor packet or annihilated; no transition creates two live
   casualties or changes any other unresolved packet;
6. every \(s_o\)-\(t\) path composes to a closed factor-feasible compound
   which preserves the marked bank, topology and all declared guards; and
7. every capacity-feasible path family commutes and its simultaneous literal
   installation has the sum of their declared physical/cap costs; and
8. the representation is complete for its declared atlas: every
   simultaneous repair admitted by that atlas decomposes into the
   represented source-to-terminal paths.

Condition 5 is the **nonbranching casualty condition**.  The toggle
\(00\to10\) in Theorem 2.1 violates it: it repairs \(b\) while exposing
both \(c\) and \(d\).

The resource construction may be a time-expanded network.  Thus a path may
contain neutral routers and may visit remote fragments.  Bounded live debt
does not imply geometric locality.

### Theorem 5.2 (guarded augmenting-flow dichotomy)

Let \(m=|\mathcal O(x)|\), give each source capacity one, and let all
resource capacities be integral.  In a serializable unit-debt atlas:

1. all packets are simultaneously repairable within the declared atlas if
   and only if the maximum \(s\)-\(t\) flow has value \(m\);
2. if the maximum value is \(f<m\), an integral minimum cut of capacity
   \(f\) is an exact guarded expansion obstruction;
3. with nonnegative arc costs, a minimum-cost value-\(m\) flow is integral,
   and if its cost exceeds the available exact cap/compiler reserve
   \(\sigma\), the min-cost-flow dual certifies the cost obstruction; and
4. every routed packet strictly lowers \(\Phi_w\) by its terminal weight at
   completed-path boundaries.  Internal arcs need not lower it.

#### Proof

Integral max-flow/min-cut and the completeness clause give (1)--(2), and
integral min-cost flow gives (3).  By Definition 5.1, each flow path is one
closed legal compound; capacity-feasible paths respect every declared
resource multiplicity and commute.  Each completed
path annihilates exactly its source debt and creates none, proving (4).
\(\square\)

Equivalently, for every set \(X\) of packet sources, every cut separating
\(X\) from \(t\) must have capacity at least \(|X|\).  This is the exact
switch-expansion condition.

### Corollary 5.3 (weighted leave)

Allow a packet to be dropped at cost \(w(o)\), and lexicographically
minimize:

\[
 \left(
   \sum_{o\text{ dropped}}w(o),\
   \text{physical/cap cost of routed paths}
 \right).                                                     \tag{5.1}
\]

The augmented integral-capacity min-cost network has an integral optimum.  If
its first coordinate is at most \(H\) and its second coordinate is at most
\(\sigma\), the completed state has terminal literal debt at most \(H\).

If every packet has \(w(o)\le b\) and the ordinary source deficiency is

\[
 \delta=\max_X\bigl(|X|-\lambda(X,t)\bigr),                    \tag{5.2}
\]

where \(\lambda(X,t)\) is the minimum \(X\)-to-\(t\) cut capacity, then
the crude bound \(H\le b\delta\) holds after a maximum-cardinality routing.
Without a uniform \(b\), constant \(\delta\) does not imply constant
literal leave.

### Corollary 5.4 (direct-bank degree test)

In the special bipartite packet-to-closed-macro graph, suppose every
nonexceptional packet has post-guard degree at least \(D\), while every
macro has degree at most \(D\).  Then Hall holds on all nonexceptional
packets.

If at most \(g\) candidates can be deleted from each packet by all later
guards, raw left degree at least \(D+g\) suffices.

#### Proof

For every left set \(X\),

\[
       D|X|\le e(X,N(X))\le D|N(X)|,
\]

so \(|N(X)|\ge|X|\).  The robust statement follows after deleting at most
\(g\) incident candidates per packet.  \(\square\)

This degree test is sufficient, not necessary.  It is meaningful only
after columns are closed macros and every guard has been applied.

## 6. The exact matroidal Hall extension

Unit-capacity path resources naturally give a strict gammoid.  Some
catalogues are more conveniently stated directly in that language.

Let \(E\) be a set of closed guarded repair macros.  Let \(M\) be a matroid
on \(E\) such that an independent set is simultaneously physically
installable.  For every packet \(o_i\), let \(A_i\subseteq E\) be its
repairing macros.

### Theorem 6.1 (guarded Rado theorem)

There is a choice

\[
                   e_i\in A_i\quad(1\le i\le m)
\]

whose members are distinct and independent in \(M\) if and only if

\[
 r_M\left(\bigcup_{i\in X}A_i\right)\ge |X|
       \qquad\text{for every }X\subseteq[m].                    \tag{6.1}
\]

With additive macro costs, a minimum-cost such choice is an integral
weighted matroid-intersection problem.  A failed inequality (6.1) is the
exact matroidal Hall cut.

#### Proof

This is Rado's independent-transversal theorem.  One proof takes a copy
\((i,e)\) for \(e\in A_i\), intersects the partition matroid allowing at
most one copy per \(i\) with the parallel extension of \(M\), and applies
the matroid-intersection min-max theorem.  Its rank inequalities reduce
exactly to (6.1).  The weighted matroid-intersection theorem gives the
minimum-cost statement.  \(\square\)

### Theorem 6.2 (exact guarded Rado deficiency)

The maximum number \(q\) of obligation packets which can receive distinct
representatives independent in \(M\) is

\[
 q=\min_{X\subseteq[m]}
       \left(m-|X|+
       r_M\left(\bigcup_{i\in X}A_i\right)\right).              \tag{6.2}
\]

Equivalently, the unmatched packet count is exactly

\[
 m-q=
 \max_{X\subseteq[m]}
 \left(
 |X|-r_M\left(\bigcup_{i\in X}A_i\right)
 \right).                                                       \tag{6.3}
\]

In particular, if

\[
 r_M\left(\bigcup_{i\in X}A_i\right)\ge\gamma|X|
 \quad\text{for every }X,                                      \tag{6.4}
\]

then at least \(\gamma m\) packets can be repaired simultaneously.

#### Proof

For any \(X\), at most
\(r_M(\bigcup_{i\in X}A_i)\) packets in \(X\) can receive independent
representatives, and at most \(m-|X|\) packets lie outside \(X\).  This
proves the upper bound in (6.2).

Let the right side of (6.3) be \(d\).  Adjoin \(d\) freely independent
dummy elements to \(M\), and put every dummy element in every candidate
set.  For every nonempty \(X\),

\[
 r_{M'}\left(\bigcup_{i\in X}A_i\cup D\right)
 =r_M\left(\bigcup_{i\in X}A_i\right)+d\ge|X|.
\]

For \(X=\varnothing\), Rado's inequality is trivial.  Theorem 6.1 gives a
full independent transversal in \(M'\).  At most \(d\)
of its representatives are dummy, so at least \(m-d\) are genuine.  This
matches the upper bound.  Formula (6.4) makes \(d\le(1-\gamma)m\).
\(\square\)

If the packets partition all active unit-weight defects,
\(w(O_i)=|O_i|\), and every packet has size at most \(L\), (6.4) gives a
batch with

\[
                 \Phi_w(Z')\le
                 \left(1-\frac{\gamma}{L}\right)\Phi_w(Z).      \tag{6.5}
\]

This is contraction at completed-batch boundaries, not along every atomic
switch.

### Proposition 6.3 (individual safety plus Hall is insufficient)

Suppose a protected target \(Y\) has exactly two provider occurrences.
Let two commuting switches repair two different holes, each withdraw one
of the two \(Y\)-providers, and add no \(Y\)-provider.  Each switch is
individually provider-safe, and the two-obligation candidate graph has a
perfect matching.  Their simultaneous selection uncovers \(Y\).

Thus provider withdrawals must be represented by capacity tickets, a joint
guard matroid, or the full state graph.  Testing the monoid derivative of
each candidate separately does not establish the hypotheses of Theorems
5.2 or 6.1.

### Proposition 6.4 (orthogonal min-cost Hall dual)

If the joint guard matroid is free, let \(c_{ie}\) be the cost of assigning
closed macro \(e\in A_i\) to packet \(i\).  Provided ordinary Hall holds,
the minimum full-repair cost equals

\[
 \max_{\alpha,\beta}
 \left(\sum_i\alpha_i-\sum_e\beta_e\right)                    \tag{6.6}
\]

over

\[
 \alpha_i-\beta_e\le c_{ie}\quad(e\in A_i),
 \qquad \beta_e\ge0,                                          \tag{6.7}
\]

with \(\alpha_i\) unrestricted.  Hence a feasible dual of value greater
than the exact reserve \(\sigma\) is a checkable certificate that every
full guarded repair costs more than \(\sigma\).

#### Proof

The primal is the bipartite minimum-cost matching program with equality one
at every packet and capacity one at every macro.  Its matrix is totally
unimodular.  Linear-programming duality gives (6.6)--(6.7), and integrality
gives the exact integer optimum.  \(\square\)

If \(M\) is the gammoid of resource-disjoint guarded routes, Theorem 6.1
is the path version of Theorem 5.2.  If selected independent macros
commute, protect every old witness, and share one terminal common-cap
acceptance state, a nonempty selection strictly lowers \(\Phi_w\).

The theorem does not apply merely because every atomic column is an
alternating incidence exchange.  Owner balance, one-cycle connectivity,
grouped cap constraints, or branching shadow casualties can destroy
heredity.  Proposition 3.1 is the smallest balance warning.  A genuinely
nonmatroidal catalogue requires the full state cut of Theorem 4.1 or a
larger exact integer master.

## 7. Regenerative physicalization and \(B(k)+O(1)\)

Suppose a physicalization at dimension \(k\) has base length
\(B(k)+c_k\).  Assume a guarded flow/Rado repair leaves unmatched packets
\(L_k\).  Let \(H_k^{\rm mid}\) be terminal missing middle masks, and let
\(H_k^0\) be all other explicitly declared terminal holes not charged to
the packets.
Assume:

1. every middle mask outside \(H_k^{\rm mid}\) is physically realized;
2. the final row is replay exact outside \(L_k\);
3. every upper target through the tracked depth is covered outside \(L_k\);
4. every deeper target has a batch-protected witness;
5. the final common cap is exact for all nonhole lower targets; and
6. \(\sum_{o\in L_k}w(o)\le H_k\); and
7. every unresolved packet \(o\) has an explicit literal casualty set
   \(T(o)\), with \(|T(o)|\le w(o)\), such that the materialized word
   covers every target outside

   \[
    H_k^{\rm mid}\cup H_k^0\cup
       \bigcup_{o\in L_k}T(o).                                  \tag{7.0}
   \]

### Theorem 7.1 (weighted guarded repair implication)

Under these hypotheses,

\[
 \nu(k)\le
 B(k)+c_k+H_k+|H_k^{\rm mid}|+|H_k^0|.                         \tag{7.1}
\]

#### Proof

By (7.0), the repaired physical word realizes every target except a union
of at most \(H_k+|H_k^{\rm mid}|+|H_k^0|\) distinct literal masks.  Append
one nonempty letter equal to each missing mask.  Appending destroys no old
interval witness.
\(\square\)

### Corollary 7.2 (uniform regenerative spine)

Suppose one compatible infinite odd Pascal/PBBS spine has, in every odd and
even child:

\[
 c_k\le c,\quad H_k\le H,\quad
 |H_k^{\rm mid}|\le h_{\rm mid},\quad |H_k^0|\le h_0,          \tag{7.2}
\]

and the selected compound routes export the same bounded sidecar
conditions needed for the next transition.  Then

\[
 \nu(k)\le B(k)+c+H+h_{\rm mid}+h_0.                           \tag{7.3}
\]

for every dimension on the spine.  The error is paid separately in each
terminal word and does not accumulate with dimension.  If
\(c=H=h_{\rm mid}=h_0=0\), the deadline lower bound gives
\(\nu(k)=B(k)\).

The middle-hole term is terminal only when the next auxiliary transition
does not use those missing owners.  An exported ordered-four-transversal,
palette, or occurrence state must itself satisfy the declared bounded
regenerative invariant.  Appending its missing masks to the terminal word
does not repair that sidecar state.

The live route length and total packet size may grow.  What must remain
bounded is the physical overhead, terminal literal leave, and unresolved
interface debt exported to the next dimension.  A fixed number of
unresolved packets is not enough unless their total literal weight is
bounded.  In particular, one unresolved residence packet can cost
\(\Theta(d(k))=\Theta(\sqrt k)\) literal targets.

## 8. Exact scope on the current \(K17\) catalogues

For the authenticated OPTIMAL28 connected owner cycle, the canonical
two-bank row currently has

\[
 |\operatorname{Def}_2|=3759,\qquad
 (|H_{10}|,|H_{11}|,|H_{12}|)=(1900,911,128),                  \tag{8.1}
\]

so the unweighted calibration is \(6698\).  This is not a terminal
literal-weight calculation.

Two catalogues must be distinguished.

1. On the frozen residual-pair skeleton, \(724\) strict runs are internal
   to \(257\) immutable components, and \(218\) rank-ten targets have no
   residual-pair provider.  Thus that scoped guarded graph has isolated
   packets and fails expansion.
2. The complete marked-preserving same-lower-colour rethread catalogue has
   \(545721\) off-source columns, and every current rank-ten hole has
   individual support.  This removes the isolated-target projection only.
   The columns still have to satisfy owner balance, one-cycle topology,
   run/shadow guards, deep-witness protection, and one common cap.  Raw
   column support is not Theorem 5.2 or 6.1.

Moreover the current row has \(3759\) unhosted row-bit obligations and no
exact common cap to transport.  The five-row cap-transport theorem is
therefore not a bootstrap.  A repaired chronology must first pass exact
inversion and upper replay, after which either a terminal common-cap
acceptance state or a guarded cap recourse bank must be proved.

The scalar reserve \(3293\), the rank-ten/-eleven/-twelve hole totals, and
current completeness at ranks thirteen and above prove none of the
network, weighted-leave, cost, deep-guard, or regenerative hypotheses.
They are calibration data only.

## 9. Sharp remaining theorem

The exact missing all-dimension statement can now be written without a
hidden local-descent assumption.

> **Guarded regenerative packet expansion.**  For one explicit
> PBBS/Pascal family, construct after all owner, topology, run, shadow,
> deep-provider, and cap guards either:
>
> 1. a serializable unit-debt network satisfying the weighted cut bound
>    \(H=O(1)\), including terminal middle-owner leave, and physical/cap
>    cost \(O(1)\); or
> 2. a strict-gammoid/other explicitly represented matroid of closed
>    packets satisfying the Rado inequalities with literal-weighted leave
>    \(O(1)\);
>
> and prove that the selected batch regenerates the same bounded sidecar
> state in the Pascal child.

This theorem would imply \(B(k)+O(1)\) by Corollary 7.2.  Zero leave and
zero overhead would imply equality.  Its failure must be exhibited by one
of:

* a guarded state sublevel cut;
* an integral network min-cut;
* a min-cost dual exceeding the true cap reserve;
* a Rado rank-deficient packet family; or
* a proof that the physical packet system is nonserializable or
  nonmatroidal.

An ordinary target-to-atomic-switch Hall table is not a certificate in
either direction.

## 10. Proven and conditional boundary

Unconditionally proved here:

* exact finite run/shadow monoid state and its required deep-guard scope;
* a minimal two-toggle counterexample to strict atomic descent;
* a counterexample against every fixed packet radius;
* the literal \(J(7,3)\) balance-closure obstruction;
* the exact global sublevel reachability cut;
* max-flow/min-cost repair under the serializable unit-debt hypothesis;
* Rado's exact matroidal Hall criterion for closed guarded macros; and
* the weighted bounded-defect implication to \(B(k)+O(1)\).

Not proved:

* that the complete marked-preserving \(K17\) catalogue has the unit-debt
  or gammoid structure;
* that its protected weighted cut leave or cap cost is bounded;
* that a fixed truncation controls all deeper shadows;
* that the present nonreplaying row has a common cap; or
* an unconditional \(K17\), \(B(k)+O(1)\), or equality theorem.
