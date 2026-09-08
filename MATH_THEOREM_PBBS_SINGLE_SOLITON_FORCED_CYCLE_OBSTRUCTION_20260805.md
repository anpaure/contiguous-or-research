# The PBBS single-soliton component is a forced q1 cycle

**Date:** 2026-08-05  
**Method:** pure cyclic-parenthesis algebra; no computation or search  
**Status:** unconditional for every `m>=3`.  The canonical max-height q1
section, and in fact every one-occurrence q1 section of the centered PBBS
factor, contains one whole `f^2`-cycle.  Therefore the PBBS occurrence
factor has no graphic q1 transversal.  This is an exact obstruction to the
cycle-hit premise of the q2 Pascal turn-section lift; it does not obstruct
an ambient Johnson/Pascal surgery which changes the carrier.

## 1. Setup

Put

\[
 n=2m+1
\]

and let `f` be the canonical cyclic-parenthesis/PBBS permutation on
`binom([n],m)`.  Write

\[
 e_X=\{f^{-1}(X),f(X)\},\qquad
 K(X)=f^{-1}(X)\cap f(X).                         \tag{1.1}
\]

The centered edges `e_X` form the natural step-two factor, whose directed
successor on rank-`m` states is `g=f^2`.  A q1 section chooses exactly one
edge occurrence of every member of `binom([n],m-1)`.

For a rank-`(m-1)` word `K`, put `T=[n]\setminus K` and define

\[
 \alpha_K(u)=r_+(K+u),\qquad
 \beta_K(u)=r_-(K+u)\qquad(u\in T),                \tag{1.2}
\]

where `r_+` and `r_-` are the forward- and reverse-unmatched zeros.
The audited PBBS first-shadow theorem gives the exact occurrence
correspondence

\[
 \mu(K)=|\operatorname {Fix}(\beta_K\alpha_K)|.    \tag{1.3}
\]

It also gives

\[
 \alpha_K(T)\subseteq U_+(K),\qquad
 \beta_K(T)\subseteq U_-(K),                       \tag{1.4}
\]

where `U_+(K),U_-(K)` are the three forward and reverse unmatched zeros
of `K`.

## 2. The single-soliton PBBS component

Represent a middle state by its forward-unmatched zero followed by its
rooted Dyck word.  Consider

\[
 A=(0_r,\,D),\qquad D=1^m0^m.                      \tag{2.1}
\]

The rooted PBBS formula marks the final up-step of the first half.  Hence

\[
 \phi(D)=\overline{0^m}\,0\,\overline{1^{m-1}}
        =1^m0^m=D,                                  \tag{2.2}
\]

while the physical root advances by `m`.  Since
`gcd(m,2m+1)=1`, the `f`-orbit of `A` has length exactly `n`; because `n`
is odd, its `g=f^2`-orbit is the same `n`-cycle.  Call it
`mathscr C_ss`.

The two-step distinguished-deletion formula says that the outgoing q1
turn at `A` is obtained by deleting the first up-step which reaches the
global height of `D`.  For the mountain (2.1), this is its final up-step.
Thus, after cyclic rotation, its q1 colour is

\[
 K=1^{m-1}0^{m+2}.                                 \tag{2.3}
\]

The q1 colours around `mathscr C_ss` are the `n` rotations of (2.3), and
they are pairwise distinct.  No coprimality assertion is needed: the word
`1^(m-1)0^(m+2)` has exactly one positive run and exactly one zero run, so
no nonidentity rotation fixes it.  Hence its orbit has length `n`.

## 3. The consecutive q1 colour has multiplicity one

Label the `m+2` consecutive zeros of (2.3), from left to right after the
one-run, by

\[
 z_0,z_1,\ldots,z_{m+1}.                            \tag{3.1}
\]

Ordinary cyclic cancellation gives

\[
 U_+(K)=\{z_{m-1},z_m,z_{m+1}\},\qquad
 U_-(K)=\{z_0,z_1,z_2\}.                            \tag{3.2}
\]

If `u` is a fixed point of `beta_K alpha_K`, then (1.4) forces

\[
 u\in U_-(K)=\{z_0,z_1,z_2\}.                      \tag{3.3}
\]

Assume `m>=3`.  For each `a in {0,1,2}`, flip `z_a` to one.  In the
resulting word, cancel first the new one with the following zero, then the
`a` intervening zeros with the last `a` old ones.  The remaining
`m-1-a` old ones cancel the next `m-1-a` zeros.  The unique surviving
forward zero is always the final one:

\[
 \alpha_K(z_a)=z_{m+1}\qquad(a=0,1,2).             \tag{3.4}
\]

Now flip `z_(m+1)` to one and run reverse cancellation.  The new terminal
one cancels `z_m`; the remaining `m-1` old ones cancel cyclically against
`z_(m-1),z_(m-2),...,z_1`.  Thus

\[
 \beta_K(z_{m+1})=z_0.                             \tag{3.5}
\]

Equations (3.3)--(3.5) show

\[
 \operatorname {Fix}(\beta_K\alpha_K)=\{z_0\},
 \qquad
 \boxed{\mu(K)=1}.                                 \tag{3.6}
\]

Rotation commutes with PBBS, so every q1 colour on `mathscr C_ss` also
has global multiplicity one.

## 4. The max-height rule is forced on this cycle

The deficit-three decomposition of (2.3) consists of one nonempty Dyck
block

\[
 1^{m-1}0^{m-1}
\]

and two empty blocks.  The nonempty block is uniquely tallest.  The
max-height representative rule therefore selects its occurrence, which is
the outgoing edge of (2.1).  Rotation gives the same conclusion at every
edge of `mathscr C_ss`.

This observation is stronger than needed: (3.6) says that *every* q1
section, regardless of its representative rule, is forced to select these
edges.

## 5. Exact obstruction theorem

### Theorem 5.1 (forced-cycle obstruction)

For every `m>=3`, every one-occurrence q1 section of the centered PBBS
step-two factor contains the entire cycle `mathscr C_ss`.  In particular,
its selected representative subgraph is not acyclic, and its omitted
occurrences do not meet every `f^2`-cycle.

#### Proof

The `n` edge colours of `mathscr C_ss` are distinct by Section 2 and each
has its only PBBS occurrence on that cycle by Section 3.  A q1 section
must retain every one of them.  `square`

### Corollary 5.2 (singleton omission-Hall cut)

In the exact PBBS omission-Hall system, take the one-cycle cut
`mathscr S={mathscr C_ss}`.  Every colour incident with this cycle has
multiplicity `mu_R=1` and omission capacity `q_R=mu_R-1=0`.  Therefore

\[
 \sum_R\min\{q_R,n_R(\mathscr S)\}=0<1=|\mathscr S|. \tag{5.1}
\]

Thus the graphic-transversal failure is certified by a support-minimal
Hall cut.  It is not a failure of scalar omission capacity elsewhere in
the factor.

### Corollary 5.3 (scope of any repair)

No change of occurrence representatives inside the fixed PBBS factor can
repair the cycle-hit condition, even if one abandons the max-height rule.
Any successful bounded repair must change the ambient carrier so that at
least one of the `n` rigid colours (2.3), or a replacement q1 colour in a
palette-preserving exchange, acquires an occurrence outside
`mathscr C_ss`.  If q2 completeness is to survive, the repair must also
retain or recreate the two adjacent selected-turn witnesses at its cut.

This is a necessary interface statement, not a construction of that
ambient repair.

## 6. All rectangular soliton cycles

The action-angle census contains one minimum `n`-cycle for every
rectangular soliton partition

\[
 \lambda=(u^b),\qquad ub=m.                         \tag{6.1}
\]

These cycles also have a direct rooted-Dyck representative.  Put

\[
 D_{u,b}=(1^u0^u)^b.                                \tag{6.2}
\]

The first global maximum is reached by the last up-step in the first
mountain.  Direct substitution in the rooted update gives

\[
\begin{aligned}
 \phi(D_{u,b})
 &=\overline{,0^u(1^u0^u)^{b-1}\}\,0\,
   \overline{1^{u-1}}\\
 &=1^u(0^u1^u)^{b-1}0^u
  =(1^u0^u)^b=D_{u,b}.                              \tag{6.3}
\end{aligned}
\]

The root advances by `u`; `gcd(u,n)=1` because `u|m` and
`gcd(m,2m+1)=1`.  Hence (6.2) indeed generates one minimum `n`-cycle.

Remove the distinguished final up-step of the first mountain to form its
outgoing q1 colour.  Its deficit-three decomposition has block heights

\[
                       (u-1,,0,,u)                \tag{6.4}
\]

when `b>=2`: the first block is `1^(u-1)0^(u-1)`, the second is empty,
and the last contains `(1^u0^u)^(b-1)`.  Therefore the outgoing occurrence
is **not** a max-height representative.  The genuinely tallest last block
also supplies a different occurrence of the same colour, so this colour
is not rigid.

When `b=1`, (6.4) becomes `(m-1,0,0)` and Sections 2--4 apply.  We have
therefore proved:

### Proposition 6.1 (rectangular-sector classification)

Among all canonical rectangular PBBS minimum cycles (6.1), the
single-soliton sector `lambda=(m)` is the unique cycle whose every edge is
forced into the max-height q1 section.  Every other rectangular cycle has
all its outgoing occurrences rejected by the max-height rule and has a
second occurrence available for each displayed outgoing colour.

This proposition does not classify the nonrectangular action sectors.

## 7. Boundary case `m=2`

For `m=2`, the same single-soliton 5-cycle is selected by the max-height
rule, so the canonical section is still cyclic.  The multiplicity-one
argument changes at (3.4): the candidate `z_2` gives a second fixed point,
and the consecutive singleton q1 colour has multiplicity two.  Hence an
occurrence swap can break the 5-cycle in this exceptional dimension.

The all-dimensional obstruction proved above is the stronger `m>=3`
phenomenon: its cycle edges are globally rigid within the PBBS occurrence
factor.

## 8. Dependencies and scope

The proof uses only:

1. the exact rooted-Dyck PBBS map;
2. the two-sided distinguished-deletion formula;
3. the exact first-shadow occurrence/fixed-point bijection; and
4. elementary cyclic parenthesis cancellation.

It does not use a finite census, a solver, a generic action-angle formula,
or any unproved q3/higher-shadow statement.  It refutes only the proposed
graphic q1 transversal **inside the fixed centered PBBS factor**.  The
q2-completeness theorem for the max-height section remains valid, and an
ambient Johnson/Pascal surgery remains open.
