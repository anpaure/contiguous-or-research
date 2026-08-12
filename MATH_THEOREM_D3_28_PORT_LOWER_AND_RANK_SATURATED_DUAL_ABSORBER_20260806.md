# A 28-port lower battery and rank-saturated dual exactly absorb the `D_3` whole-factor suffix current

**Date:** 2026-08-06  
**Method:** pure mathematics; literal shielded-port calculation  
**Status:** unconditional all-width **current algebra** theorem.  The
22-channel interior current of the canonically suspended
\(\mathcal P^-\to\mathcal P^+\) macro admits an exact lower absorber with
22 main ray ports, four bottom ports, and two top-cap ports.  Mirroring those
28 ports by generalized rank-saturated complementary ports and adding six
central-only compensators cancels the complete upper current without using a
letter above rank \(m+1\).  The theorem does **not** embed these rails in one
simple resident carrier, preserve a background compiler matching, or prove an
additive-constant word.

## 1. Set-valued shielded ray ports

Let \(P,N\) be distinct sets of the same rank \(q\), let

\[
                              H=P\cup N,              \tag{1.1}
\]

and let \(Z=(z_1,\ldots,z_t)\) be an ordered list disjoint from \(H\).
Consider the two states of the block

\[
                 H,\ P_e,\ \{z_1\},\ldots,\{z_t\},\ H,
                 \qquad P_e\in\{P,N\}.               \tag{1.2}
\]

### Lemma 1.1 (set-valued lower ray)

Changing the pivot from \(P\) to \(N\) has complete interval current

\[
             \mathcal L_Z(P,N)
             =\sum_{j=0}^t
                \bigl([Z_j\cup N]-[Z_j\cup P]\bigr), \qquad
             Z_j=\{z_1,\ldots,z_j\}.                 \tag{1.3}
\]

#### Proof

An interval avoiding the pivot is fixed.  An interval containing either
shield contains \(H\), and hence has the same union in the two states.  Every
other changed interval starts at the pivot and ends after a prefix of the
rail.  These are exactly the terms in (1.3).  \(\square\)

The singleton-endpoint port is the case \(q=1\).  The same literal gadget
therefore carries the rank-two unit differences occurring in the currents
\(C,D,E,F,G\); no reduction to singleton endpoints is needed.

## 2. A general rank-saturated complementary port

Let \(|\Omega|=2m+1\), and retain the data \(P,N,H,Z\) above.  Put

\[
              R=\Omega\setminus(Z\cup H),
              \qquad r=|N\setminus P|=|P\setminus N|.          \tag{2.1}
\]

Assume

\[
                              |Z|+q\le m.             \tag{2.2}
\]

Choose

\[
              C\subseteq R,qquad |C|=m+1-r,
              \qquad K=R\setminus C.                 \tag{2.3}
\]

This is possible because

\[
 |R|-(m+1-r)=m-|Z|-q\ge0.                            \tag{2.4}
\]

Use the two rank-\((m+1)\) pivot letters

\[
              Q_P=C\cup(H\setminus P)=C\cup(N\setminus P),
              \qquad
              Q_N=C\cup(H\setminus N)=C\cup(P\setminus N).   \tag{2.5}
\]

The anchor \(K\) is used as **one set-valued letter**, even when it has more
than one coordinate.  Consider

\[
 H,\ Q_e,\ K,\ \{z_t\},\{z_{t-1}\},\ldots,\{z_1\},\ H,
 qquad Q_e\in\{Q_P,Q_N\}.                            \tag{2.6}
\]

### Lemma 2.1 (arbitrary equal-rank saturated dual)

The transition \(Q_P\to Q_N\) has complete current

\[
\boxed{
 [Q_N]-[Q_P]
 +\sum_{j=0}^t
   \left(
    [\Omega\setminus(Z_j\cup N)]
    -[\Omega\setminus(Z_j\cup P)]
   \right).}                                         \tag{2.7}
\]

Every pivot has rank \(m+1\).  The anchor letter has rank
\(m-|Z|-q\le m\), and no letter in the port has rank above \(m+1\).

#### Proof

Both unions \(H\cup Q_P\) and \(H\cup Q_N\) equal \(C\cup H\), so any
interval meeting a shield is fixed.  The pivot singleton contributes the
first two terms of (2.7).  Moreover

\[
\begin{aligned}
 Q_P\cup K&=R\cup(H\setminus P)=\Omega\setminus(Z\cup P),\\
 Q_N\cup K&=R\cup(H\setminus N)=\Omega\setminus(Z\cup N).
\end{aligned}                                        \tag{2.8}
\]

After appending \(z_t,\ldots,z_{j+1}\), these become respectively
\(\Omega\setminus(Z_j\cup P)\) and
\(\Omega\setminus(Z_j\cup N)\).  These are all remaining changed
intervals.  The rank assertions follow from (2.3)--(2.5).  \(\square\)

The set-valued anchor is important.  If \(|K|>1\) and its coordinates were
inserted one at a time, unwanted intermediate upper currents would appear.
One anchor letter jumps directly from the central pivot to the required
complementary ray.

### Lemma 2.2 (central-only reverse port)

The reverse transition

\[
                         H,Q_N,H\ \longrightarrow\ H,Q_P,H     \tag{2.9}
\]

has the sole current \([Q_P]-[Q_N]\).

#### Proof

The pivot singleton changes as displayed.  Every longer interval containing
the pivot meets a shield and contains the common set \(C\cup H\).  \(\square\)

Thus every saturated dual ray can have its owner-shore singleton current
cancelled by one bounded central-only port if no opposite dual ray is already
available.

## 3. Unit decompositions of the eight base currents

Use the currents \(A,\ldots,G\) from
`MATH_THEOREM_D3_WHOLE_FACTOR_SUFFIX_CURRENT_AND_22_RAY_BATTERY_GATE_20260806.md`.
An arrow \(P\to N\) denotes the lower-port transition whose current is
\([N]-[P]\), namely the negative of the unit current \([P]-[N]\).

Choose the following decompositions:

\[
\begin{array}{c|l}
\text{current}&\text{battery arrows }P\to N\\ \hline
A&3\to2,\quad3\to2,\quad5\to4\\
B&2\to3,\quad4\to5,\quad4\to5\\
C&35\to24,\quad15\to14\\
D&24\to35,\quad25\to15,\quad14\to34\\
E&35\to24,\quad36\to26,\quad25\to34\\
F&24\to35,\quad26\to36\\
G&34\to25.
\end{array}                                                   \tag{3.1}
\]

For example, the three arrows in the first row sum to

\[
                   2[2]+[4]-2[3]-[5]=-A.             \tag{3.2}
\]

The other rows are read identically.

## 4. The exact 28-port lower absorber

Use the bank notation

\[
 U=(u_1,\ldots,u_s),\qquad
 W=(v_1,\ldots,v_s,\infty).                          \tag{4.1}
\]

For a suffix profile, order the ray backwards so that its prefixes are the
desired suffix sets.

### 4.1 The twenty-two main rays

Install the arrows in (3.1) on the following eight profile families:

\[
\begin{array}{c|c|c|c}
\text{family}&\text{base current}&\text{profiles}&\text{number of ports}\\ \hline
D\text{-prefix},q=1&A&W_t^+,\ 0\le t\le s+1&3\\
D\text{-suffix},q=1&B&U_t^-,\ 0\le t\le s&3\\
I\text{-prefix},q=1&A&U_t^+,\ 0\le t\le s&3\\
I\text{-suffix},q=1&B&W_t^-,\ 0\le t\le s+1&3\\
D\text{-prefix},q=2&C&W_t^+,\ 0\le t\le s&2\\
D\text{-suffix},q=2&D&U_t^-,\ 0\le t\le s&3\\
I\text{-prefix},q=2&E&U_t^+,\ 0\le t\le s&3\\
I\text{-suffix},q=2&F&W_t^-,\ 0\le t\le s&2.
\end{array}                                                   \tag{4.2}
\]

The four \(q=1\) families have an unwanted rank-one term at \(t=0\).  Their
aggregate is

\[
                         -2(A+B)                       \tag{4.3}
\]

in battery orientation.  In each of the \(W\)- and \(U\)-groups, the
decompositions of \(A\) and \(B\) have the reverse pairs

\[
                 3\to2\ \leftrightarrow\ 2\to3,
                 \qquad
                 5\to4\ \leftrightarrow\ 4\to5,     \tag{4.4}
\]

and leave the two arrows \(3\to2\) and \(4\to5\).

### 4.2 Four bottom ports

Add, once for the \(W\)-group and once for the \(U\)-group, the two
zero-length lower ports

\[
                              2\to3,qquad5\to4.       \tag{4.5}
\]

Their total current is \(+2(A+B)\), cancelling (4.3).  They create no
higher-rank value.

### 4.3 Two top-cap ports

The maximal proper interval contains the additional current

\[
                              U\star G= [U34]-[U25].   \tag{4.6}
\]

Install one full \(U\)-ray with arrow \(34\to25\), and one truncated
\((u_1,\ldots,u_{s-1})\)-ray with the reverse arrow \(25\to34\).  Their
currents cancel at every prefix of length \(0,\ldots,s-1\) and leave exactly

\[
                              [U25]-[U34]=-U\star G    \tag{4.7}
\]

at the full profile.

### Theorem 4.1 (28-port proper-lower cancellation)

The 22 main ports, four bottom ports, and two top-cap ports have complete
proper-lower current

\[
                              -\Delta_\ell            \tag{4.8}
\]

at every rank \(1\le\ell\le m-1\), where \(\Delta\) is the suffix current
of the whole-factor macro.  No changed value has rank \(m\) or larger.

#### Proof

For ranks \(2,\ldots,m-2\), Lemma 1.1 and table (4.2) give the negative of
the eight-rail formula for \(\Delta_\ell\).  The four bottom ports cancel
the unwanted \(t=0\) rank-one current.  At rank \(m-1\), the full and
truncated top ports contribute precisely (4.7), while all other main rays
give the four remaining terms in the maximal-profile formula.  Hence the
sum is \(-\Delta\) rank by rank.

Every main or top value has rank at most \(2+s=m-1\), and the bottom values
have rank one.  \(\square\)

Within the independent capacity-one ray model this count is sharp: 22 main
ports are forced by the generic interior positive mass, four units are
forced by the rank-one residual, and a nonzero top-only ray difference needs
one full and one reverse truncated port.  A higher-valence non-ray gadget
could evade this restricted minimality statement.

## 5. Rank-saturated dualization and exact central cancellation

Mirror every one of the 28 lower ports by Lemma 2.1, using the same arrow
\(P\to N\) and the same full rail set.  Its proper-upper current is the
complement of that lower-port current.  Therefore the 28 dual rays have
aggregate proper-upper current

\[
                              -\overline\Delta.        \tag{5.1}
\]

It remains only to cancel their rank-\((m+1)\) pivot singletons.

The cores \(C\) may be selected so that every reverse pair in (4.4) uses the
same \(C\) and hence the same two pivot letters.  Pair the two residual
\(q=1\) arrows with their reverse bottom ports, again using the same core.
Thus all sixteen \(q=1\) dual pivot currents cancel.

For the two top-cap rays, choose one common core contained in
\(\Omega\setminus(U\cup\{2,3,4,5\})\).  The full and truncated rays have
opposite arrows and therefore cancel their dual pivot currents as well.

For the \(q=2\) main rays, use the reverse pairs

\[
 \begin{array}{c|c}
 W\text{-side}&35\to24\ \leftrightarrow\ 24\to35,\\
 U\text{-side}&24\to35\ \leftrightarrow\ 35\to24.
 \end{array}                                                   \tag{5.2}
\]

On the \(W\)-side the two full profile sets are \(W_s^+\) and \(W_s^-\).
Their union is \(W\), and

\[
 \left|\Omega\setminus(W\cup\{2,3,4,5\})\right|=m-1,          \tag{5.3}
\]

exactly the required common-core size.  On the \(U\)-side the profile set is
the same full \(U\)-bank, so a common core is immediate.

After these cancellations, the six unpaired \(q=2\) arrows are

\[
\begin{array}{c|l}
W\text{-side}&15\to14,\quad26\to36,\\
U\text{-side}&25\to15,\quad14\to34,
               \quad36\to26,\quad25\to34.
\end{array}                                                   \tag{5.4}

For each, add the central-only reverse port of Lemma 2.2 with the same
\(H,C,Q_P,Q_N\).  These six ports cancel the remaining pivot singleton
currents and create no other current.

### Theorem 5.1 (rank-saturated complete-current absorber)

Combine:

1. the canonically suspended whole-factor transition
   \(\widehat{\mathcal P^-}\to\widehat{\mathcal P^+}\);
2. the 28 lower ports of Theorem 4.1;
3. their 28 rank-saturated complementary dual ports; and
4. the six central-only dual compensators in (5.4).

Assume the displayed blocks are mutually shield-isolated, so every interval
meeting two blocks contains the relevant shields.  Then the total signed
interval-union current is zero at every nontrivial rank.

Every dual pivot has rank \(m+1\); every set-valued anchor has rank at most
\(m\); and every other battery letter has rank at most \(m+1\).

#### Proof

The whole-factor macro contributes \(\Delta\) below the middle and
\(\overline\Delta\) above it, while preserving the two central palettes.
Theorem 4.1 contributes \(-\Delta\) and nothing at or above the middle.
The 28 dual rays contribute \(-\overline\Delta\), together with their
central pivot singleton currents.  The reverse-pair choices, bottom and top
pairings, and six applications of Lemma 2.2 cancel those singleton currents
exactly.  Shield isolation removes all cross-block currents.  Therefore the
sum vanishes rank by rank.  The rank bounds follow from Lemma 2.1 and the
listed lower-port ranks.  \(\square\)

## 6. Exact scope

The current algebra is now closed by a bounded interface:

\[
 \boxed{
  22\text{ main lower rays}
  +4\text{ bottom ports}
  +2\text{ top ports}
  +28\text{ saturated dual rays}
  +6\text{ central compensators}.}                  \tag{6.1}
\]

The rail interiors have total length \(O(m)\), not \(O(1)\).  For an
additive-constant theorem they must replace existing chronology support; only
their bounded pivots, shields, and junction state may be charged as extra
positions.  The still-open statement is therefore a protected
coinstantiation theorem: plant these rails together with the pentagon macro,
residence, q1 palettes, and one background compiler basis in a simple carrier.

No further lower/upper current identity is missing.  The obstruction after
this theorem is physical host supply and occurrence-level common-cap
compatibility, not current arithmetic.
