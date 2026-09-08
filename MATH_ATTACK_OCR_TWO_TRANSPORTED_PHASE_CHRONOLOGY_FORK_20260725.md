# Two transported PBBS phases: the reset telescope and the exact chronology fork

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, or solver

## 0. Result

Fix two phases (0\le t<u<s), put

\[
 d=u-t,
 \qquad S=s-d-1,
\]

and retain the exact transported tail equation

\[
 A R_t=R_u C,                                    \tag{0.1}
\]

where

\[
 A=(\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 C=(0S_u)\cdots(0S_{t+1}).                       \tag{0.2}
\]

This note proves four exact facts.

1. The terminal reset sink at either phase accepts every record state
   generated at that phase.  Conditional on the two incoming reset
   conditions, intersecting the transported sink sets removes no word.
   Thus two terminal resets telescope; they do not give two independent
   projections.

2. Put

   \[
   \Delta=|R_u|-|A|=|R_t|-|C|.
   \]

   If (Delta\ge0), there is a unique common middle word (Z) with

   \[
   R_u=AZ,
   \qquad R_t=ZC.                                 \tag{0.3}
   \]

   It has net height (-S).  For collars legal at their required
   baselines, its exact free-corridor series is

   \[
   G_S(x)={x^S\over F_{S+1}(x^2)}.                \tag{0.4}
   \]

   If (d\le(1-\varepsilon)s), this sector retains a central scalar
   renewal Green mass (Theta_\varepsilon(s)).

3. If (Delta=-r<0), there is instead a unique overlap bridge (H)
   with

   \[
   A=R_uH,
   \qquad C=HR_t,                                 \tag{0.5}
   \]

   and

   \[
   \operatorname{net}(H)=S,
   \qquad r\ge S,
   \qquad r\equiv S\pmod2.                       \tag{0.6}
   \]

4. For an actual zero-winding staircase, this word dichotomy has the
   exact endpoint-overlap ledger

   \[
   \boxed{\Delta=B_{t,u}-\Lambda,}                \tag{0.7}
   \]

   where

   \[
   B_{t,u}
   =\sum_{0\le j<t}(|T_j|+1)
    +\sum_{u<j<s}(|S_j|+1)                         \tag{0.8}
   \]

   is the total length of the two omitted outer collars and

   \[
   \Lambda=\delta(D_0)+\delta(D_s)-2m.
   \]

   Consequently every actual compatible phase pair obeys the forbidden
   window

   \[
   \boxed{|B_{t,u}-\Lambda|\ge S.}                \tag{0.9}
   \]

   In the overlap branch,

   \[
   |H|=\Lambda-B_{t,u},
   \qquad \Lambda\ge B_{t,u}+S\ge2S.             \tag{0.10}
   \]

Therefore the two reset/sink sets do **not** intersect subcritically.
They telescope on every word already satisfying the transported
compatibility.  The only possible two-phase gain is either joint rarity
of the two incoming reset conditions or a coefficientwise bound for the
positive-net bridges in (0.5)--(0.6).  The nonoverlap branch itself still
contains the full critical corridor mode.

No coefficient-one conclusion is claimed.

## 1. Terminal reset sets do not multiply

The adjacent phase identities are

\[
 Q_{j+1}=S_j1Q_j,
 \qquad
 V_j=V_{j+1}1\overline T_j,
 \qquad
 S_j1P_j=P_{j+1}1\overline T_j.                  \tag{1.1}
\]

Let (E_j) be the seam event (P_j=Q_jV_j).  Substitution in (1.1)
and right cancellation give (E_j\Rightarrow E_{j+1}); the reverse
substitution and left cancellation give the converse.  Hence

\[
 E_t\Longleftrightarrow E_u.                      \tag{1.2}
\]

This is a literal free-monoid equivalence, not an asymptotic correlation.

At phase (j), let (p_j^{\rm in}) be the record height immediately
before the first outer reset word, and let (b_j) be that word's reset
depth.  Write

\[
 I_j=\{p_j^{\rm in}\le b_j\}.                    \tag{1.3}
\]

On (I_j), the first outer word resets the record to zero.  The renewal
segment produces a set (Q_j^{\rm real}) of intermediate records, and
the terminal outer word resets every element of (Q_j^{\rm real}).
Thus its sink set is the entire realized range, not a proper subset.

Let (Theta_{t,u}) be the deterministic parsing transport supplied by
(0.1) and the intervening local identities.  On the exact common-base
language,

\[
 \Theta_{t,u}^{-1}(Q_u^{\rm real})=Q_t^{\rm real}. \tag{1.4}
\]

Therefore the exact joint acceptance indicator is

\[
 \boxed{
 \mathbf1_{E_t\cap E_u\cap I_t\cap I_u}
 =\mathbf1_{E_t}\mathbf1_{I_t}\mathbf1_{I_u}.}   \tag{1.5}
\]

No terminal-sink factor remains.  The relation between
(p_t^{\rm in}) and (p_u^{\rm in}) is not asserted here; it is one of
the surviving two-phase questions.

If the two scans have a common atomization, attach to each atom its pair
of record depths and update by coordinatewise maximum.  Möbius inversion
on the product of the two record chains shows that summing the exact-state
Green function over the full realized reset range leaves only the top
cumulative term.  Hence

\[
 \sum_qG(q)={1\over1-\rho}.                       \tag{1.6}
\]

At a central seam this has critical mass (Theta(s)).  Interlaced
atomizations need a larger state, but (1.5) remains valid: reset
intersection itself removes no compatible word.

## 2. Free-monoid solution of the transported equation

Both collars in (0.2) have net height (-d), while every terminal word
(R_j) has net height (1-s).  Length equality in (0.1) gives

\[
 |R_u|-|A|=|R_t|-|C|=:\Delta.                    \tag{2.1}
\]

### 2.1 Nonoverlap

Assume (Delta\ge0).  The first (|A|) letters in (0.1) force
(R_u=AZ) for one unique word (Z).  Cancelling (A) then gives
(R_t=ZC).  Moreover

\[
 \operatorname{net}(Z)
 =(1-s)-(-d)=-S.                                  \tag{2.2}
\]

Native legality of (R_t=ZC), with (Z) read from height (s), gives

\[
 1-s\le H_Z\le0.
\]

Native legality of (R_u=AZ), where (Z) begins at height (s-d),
gives

\[
 1-(s-d)\le H_Z\le d.
\]

Their intersection is

\[
 -S\le H_Z\le0,                                   \tag{2.3}
\]

and (2.2) says that (Z) ends at the lower wall.  Thus, after vertical
translation, (Z) is exactly an endpoint-to-endpoint walk on
({0,1,\ldots,S}).  Its generating function is (0.4), by the usual
continuant minor.

Conversely, suppose explicitly that (A) is legal from height (s) to
height (s-d), and (C) is legal from height (d+1) to height one.
Then every walk (Z) satisfying (2.2)--(2.3) makes both (AZ) and
(ZC) legal terminal corridors.  Hence (0.4) is exact for these fixed
legal collars.

At (x=1/2),

\[
 G_S(1/2)={2\over S+2},
 \qquad
 {G_S(1/2)\over G_s(1/2)}={s+2\over s-d+1}.       \tag{2.4}
\]

When (S\asymp s), this is only a bounded change.  Marking a central
seam of the (S)-corridor restores a scalar renewal factor of critical
mass (Theta(S)=Theta(s)).  Thus the nonoverlap branch is not
subcritical.

### 2.1.1 Every intermediate transported phase retains the same corridor

Let \(t<v<u\), and abbreviate

\[
 a=v-t,\qquad b=u-v,\qquad a+b=d.
\]

The collars factor in their literal order as

\[
 A_{t,u}=A_{v,u}A_{t,v},
 \qquad
 C_{t,u}=C_{v,u}C_{t,v}.                          \tag{2.5a}
\]

If the endpoint phases are in the nonoverlap form

\[
 R_u=A_{t,u}Z,\qquad R_t=ZC_{t,u},
\]

then the two transported equations force

\[
 \boxed{R_v=A_{t,v}\,Z\,C_{v,u}.}                 \tag{2.5b}
\]

Indeed,

\[
 A_{t,v}R_t
 =A_{t,v}ZC_{v,u}C_{t,v}
 =R_vC_{t,v},
\]

and right cancellation gives (2.5b); the equation from \(v\) to \(u\)
then follows from (2.5a).

There is no new corridor restriction.  The prefix collar \(A_{t,v}\)
has net \(-a\), so \(Z\) starts at height \(s-a\).  Since
\(\operatorname{net}(Z)=-S\), it ends at

\[
 s-a-S=b+1.
\]

The already proved bound \(-S\le H_Z\le0\) therefore keeps this reading
of \(Z\) inside

\[
 [\,b+1,\ s-a\,]\subseteq[1,s].
\]

For collars legal at their native baselines, \(R_v\) is automatically a
legal terminal corridor.  Iterating proves the same statement for every
intermediate phase:

\[
 \boxed{
 R_v=A_{t,v}ZC_{v,u}\quad(t\le v\le u).}          \tag{2.5c}
\]

Thus a third phase between \(t\) and \(u\) commutes with the existing
transport and retains exactly the same free \(Z\)-language.  No finite
collection of intermediate reset phases can make the nonoverlap corridor
subcritical.  A useful extra phase would have to impose information not
contained in the one-dimensional tail cocycle.

### 2.2 Overlap

Assume (Delta=-r<0).  Then (R_u) is the prefix of (A) of length
(|R_u|); write (A=R_uH).  Substitute this in (0.1) and cancel (R_u)
to obtain (C=HR_t).  The word (H) is unique and has length (r).
Its net height is

\[
 \operatorname{net}(H)
 =\operatorname{net}(A)-\operatorname{net}(R_u)
 =-d-(1-s)=S.                                     \tag{2.5}
\]

Every binary word of net (S) has length at least (S) and the same
parity as (S), proving (0.6).

### 2.3 Quantitative bridge penalty

The overlap bridge has a universal critical-mass penalty before any of
its two collar constraints are imposed.  For fixed admissible (r,S),

\[
 \sum_{\substack{H:\ |H|=r\\
                   \operatorname{net}(H)=S}}
       2^{-r}
 =2^{-r}\binom r{(r+S)/2}
 \le {C\over\sqrt{r+1}}
       \exp\!\left(-c{S^2\over r}\right)
 \le {C\over\sqrt{S+1}}.                         \tag{2.6}
\]

Indeed the left side is
\(\Pr(X_1+\cdots+X_r=S)\) for independent Rademacher variables.
The standard binomial local bound gives the middle expression; its
exponential part also follows from Hoeffding, while the
(O(r^{-1/2})) prefactor follows from the central-binomial bound and the
usual ratio estimate.  Since (r\ge S), the last inequality follows.
Requiring (H) to be simultaneously a suffix of (A) and a prefix of
(C) only decreases this mass.

The estimate counts every bridge bit once: in (0.5), (H) is the literal
overlap of the two collars, not two independent copies.  Consequently the
overlap branch has an (O(S^{-1/2})=o(1)) critical factor whenever
(S\to\infty).  It is exponentially suppressed whenever (r=O(S)),
and the stronger exponential part tends to zero whenever

\[
 r=o(S^2).                                         \tag{2.7}
\]

Thus the exponential part could fail to vanish only in the quadratic
length regime

\[
 \boxed{|H|=\Lambda-B_{t,u}=\Omega(S^2).}         \tag{2.8}
\]

Even in that regime the local (O(S^{-1/2})) factor remains.  This is a
conditional critical-mass statement for the disjoint bridge
piece.  Turning it into a full coefficient bound still requires the
remaining collar and external-kernel lengths to be assembled without
duplication.

Since (r=\Lambda-B_{t,u}\le\Lambda), a useful immediate case is

\[
 S\ge\varepsilon s,
 \qquad \Lambda=o(s^2).
\]

Then (r=o(S^2)), and (2.6) gives an (o(1)) bridge factor uniformly on
that overlap branch.  Hence, below quadratic endpoint overlap, every
macroscopically separated two-phase obstruction must come from the
nonoverlap common corridor, not from an unsuppressed overlap bridge.

## 3. Exact staircase ledger

Put

\[
 d_j=|S_j|+1,
 \qquad L_h=\sum_{j<h}d_j,
\]

and

\[
 M_h=\delta(D_h)-L_h,
 \qquad e_h=M_h-M_{h+1}=|T_h|+1.                 \tag{3.1}
\]

For zero winding,

\[
 L_s=\delta(D_s),
 \qquad M_0=\delta(D_0),
 \qquad M_s=0.                                   \tag{3.2}
\]

Since

\[
 D_h=P_h1R_h0S_h,
 \qquad |P_h1|=\delta(D_h)=L_h+M_h,
\]

one has

\[
 |R_h|=2m-L_{h+1}-M_h.                            \tag{3.3}
\]

Also

\[
 |A|=\sum_{j=t}^{u-1}e_j=M_t-M_u,
 \qquad
 |C|=\sum_{j=t+1}^{u}d_j=L_{u+1}-L_{t+1}.        \tag{3.4}
\]

Substitution of (3.3)--(3.4) into (2.1) gives

\[
 \Delta=2m-L_{u+1}-M_t.                           \tag{3.5}
\]

On the other hand,

\[
 \Lambda=M_0+L_s-2m                              \tag{3.6}
\]

and

\[
 B_{t,u}
 =(M_0-M_t)+(L_s-L_{u+1}).                        \tag{3.7}
\]

Equations (3.5)--(3.7) prove (0.7).

There are exactly

\[
 t+(s-u-1)=S                                      \tag{3.8}
\]

terms in (0.8), and every term is at least one.  Hence

\[
 B_{t,u}\ge S.                                    \tag{3.9}
\]

In the nonoverlap branch, the word (Z) has length

\[
 |Z|=\Delta=B_{t,u}-\Lambda
\]

and net (-S), so (B_{t,u}-\Lambda\ge S).  In the overlap branch,

\[
 |H|=-\Delta=\Lambda-B_{t,u}
\]

and net (S), so (Lambda-B_{t,u}\ge S).  This proves (0.9)--(0.10).

### Corollary 3.1 (a forced jump in every nested phase scan)

Assume (Lambda>0).  Start with
([t_0,u_0]=[0,s-1]), and at each step delete exactly one
outer phase, so that

\[
 S_r=t_r+(s-u_r-1)=r.
\]

Let (B_r=B_{t_r,u_r}).  Then for every compatible interval

\[
 B_r\le\Lambda-r
 \quad\hbox{or}\quad
 B_r\ge\Lambda+r.                                \tag{3.10}
\]

If the branch changes between (r-1) and (r), the newly added collar
block has length

\[
 B_r-B_{r-1}\ge2r-1.                              \tag{3.11}
\]

Indeed the old interval lies below (Lambda-(r-1)), while the new one
lies above (Lambda+r).  Thus any transition from overlap to
nonoverlap pays one explicitly large (S)- or (T)-block.  If no such
transition occurs through and including the adjacent-phase interval
(r=s-2), then
the overlap inequality and (B_r\ge r) force

\[
 \Lambda\ge2(s-2).                                \tag{3.12}
\]

There is also a scale-free consequence.  At the transition, (B_r) is
the sum of exactly (r) collar-block lengths and (B_r\ge\Lambda+r).
Hence the largest of those (r) blocks is at least

\[
 \max\left\{2r-1,{\Lambda+r\over r}\right\}
 \ge \sqrt{2\Lambda}-1.                           \tag{3.13}
\]

For the last inequality, use the first term when
(r\ge\sqrt{\Lambda/2}) and the second otherwise.  Thus every actual
overlap-to-nonoverlap transition exposes one block of length
(Omega(\sqrt\Lambda)), independently of where the transition occurs.

For any *prescribed* capped Dyck block (D), its normalized critical
Boltzmann tail obeys

\[
 \Pr(|D|\ge2n)
 \le\sum_{j\ge n}\operatorname{Cat}_j4^{-j}
 \le {C\over\sqrt{n+1}}.                          \tag{3.14}
\]

The first inequality uses only that the cap removes words and that its
partition function is at least one; the second is the standard
(operatorname{Cat}_j4^{-j}=O((j+1)^{-3/2})) tail.  Thus a prescribed
transition block satisfying (3.13) has critical mass

\[
 O(\Lambda^{-1/4}).                                \tag{3.15}
\]

The transition position is selected from the block lengths themselves,
so (3.15) cannot be unioned over the (s) possible positions without
losing its force.  A position-free injection or a stopping-time tail
estimate preserving the rank ledger is required to turn this marked
factor into a root bound.

This is the exact chronology fork left for a coefficientwise attack:
charge the large transition block in (3.11), or control the persistent
macroscopic bridge sector in (3.12).

## 4. Proved boundary

Proved:

1. Two transported terminal reset sinks never multiply; conditional on
   the two source-reset events, their intersection is the whole realized
   compatibility language.
2. The nonoverlap solution has an exact common corridor and retains
   (Theta(s)) critical Green mass.
3. The overlap solution has one unique positive-net bridge.
4. For actual zero-winding staircases, the sign and length of these two
   sectors are governed exactly by (B_{t,u}-\Lambda), with the forbidden
   window and forced-jump consequences above.

Unproved:

1. A useful relation between the two incoming source records.
2. A coefficientwise tail bound for the forced block in (3.11) or the
   remaining quadratic-length bridge regime in (2.8).
3. Any constant-one conclusion.
