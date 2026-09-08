# Audit and repair of Fable's quantitative seam alternative

## 1. Scope and verdict

This note audits the candidate mathematics in assistant thinking record 78 of

`/Users/amir.nuriyev/.claude/projects/-Users-amir-nuriyev-Documents-problem/13875c1e-618a-4092-89f8-b6287f5ff29a.jsonl`.

It does not reproduce the private reasoning trace.  It reconstructs only the
proposed seam-local maximum argument and checks it against the authoritative
statements in:

- `fable_general_case/FABLE_SEAM_LEVEL_LAW_AUDIT.md`;
- `FABLE_RUN_SPECTRUM_AUDIT.md`;
- `FIRST_DANGEROUS_GLOBAL_SERVICE.md` and its audit; and
- `POSITIVE_SEAM_CROSSLINE_COUPLING.md` and its audit.

The trace itself is not a proof.  Its first genuine gap is the passage from a
cheap run attached to a seam to an asserted cubic saving: it never defines a
set of starts which are simultaneously

1. assigned to the successor plateau by the first-dangerous rule;
2. strictly outside the new run;
3. close enough that their forward windows contain the new run; and
4. disjoint from the corresponding sets for other seams.

Several later numerical claims therefore have no support as written, and one
intermediate line even alternates between `O(aD)` and `O(a^2D)` corrections.

That gap is repairable.  The seam-local maximum does give a valid internal
threshold run, and there is an exact interval of first-dangerous starts that
can be reassigned to it.  The repaired argument below proves the following
conditional theorem.

> **Atomic seam-exclusion theorem.**  In the inherited three-box setup, assume
> `D=o(a^2)` and
> \[
>   \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}
>      \Longrightarrow 2\delta_x,
>      \qquad {4\over3}\le x\le {3\over2},
> \]
> where the sum is over directed internal coordinate-peak plateaux.  Then no
> such sequence of middle orders exists.

This excludes the balanced static survivor `2 delta_(4/3)` and, in fact, the
whole displayed atomic interval.  It does **not** exclude non-atomic profiles,
does not prove the universal three-box obstruction, and does not settle the
Boolean-array problem.

## 2. Audited setup

Let

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
               |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1,
\]

and let `T_1,...,T_(M_a)` be a linear ordering of its points.  For a
coordinate `d` and an integer `t`, a maximal component of

\[
                 \{s:T_s(d)\ge t\}
\]

is a threshold run.  It is admissible in the capped-run machinery when it is
internal in the full word and does not contain the index to which it is
assigned.  It need not be a constant-coordinate plateau.

Fix a numerical threshold `1<c<x`.  The `c`-dangerous plateaux are the
directed internal coordinate-peak plateaux with edge length `lambda>ca`.
List them in word order:

\[
                    P_j=[u_j,v_j],\qquad
                    \lambda_j=v_j-u_j.
\]

Their edge sets are disjoint; consecutive plateaux can share at most one
endpoint.  Gaps use the audited vertex-union convention.  Thus for a
nonoverlapping consecutive pair

\[
       P_{j-1}=[u_-,v],\qquad P_j=[u,v_j],
       \qquad g=u-v-1,
\]

while a shared endpoint has `u=v` and `g=0`.

Put `L=4a+2`.  The audited first-dangerous assignment uses

\[
                         W_i=[i+1,i+L].
\]

If `W_i` contains a complete dangerous plateau, it assigns the first one;
otherwise it assigns a run of cost at most `ca`.  It omits only the final
`L` starts and has one-sided span and endpoint congestion at most `L+1`.

The audited run-spectrum inequality, at `h=3a-1`, implies that every such
assignment with `O(a)` omissions and span `O(a)` has total capped cost

\[
                         Q\ge(4-o(1))a^3                 \tag{2.1}
\]

when `D=o(a^2)`.  All runs used below have cost at most `2a`, so their capped
and uncapped costs agree for large `a`.

## 3. The seam-local maximum lemma

### Lemma 1 (local cap or high absorption)

Let `P=[u_-,v]` and `P'=[u,v']` be consecutive directed dangerous plateaux.
Assume both are regular in the sense

\[
       (x-\epsilon)a\le\lambda(P),\lambda(P')
                         \le(x+\epsilon)a,             \tag{3.1}
\]

where `epsilon<x-1`.  Let `d` be the strictly rising cross-coordinate on
`P`, and put

\[
       h=T_v(d),\qquad
       M=\max_{v\le s\le u}T_s(d).                      \tag{3.2}
\]

Then at least one of the following conclusions is available.

1. **High absorption.**  The fixed coordinate of `P'` is `d`, and its level
   is `M`.  In particular
   \[
        M\ge h\ge\lambda(P)-a
                   \ge(x-1-\epsilon)a.                 \tag{3.3}
   \]
2. **Seam-local run.**  There is a full-word internal threshold run
   `R subseteq [v,u]`, in coordinate `d`, with
   \[
             \lambda(R)\le u-v
              \le g+1,                                 \tag{3.4}
   \]
   where the last bound is equality for a nonoverlapping seam and remains
   safe for a shared endpoint.

#### Proof

Because `d` is a strictly increasing integer coordinate along `P`,

\[
 T_v(d)-T_{u_-}(d)\ge\lambda(P),
\]

and `T_(u_-)(d)>=-a`; hence (3.3).  Also

\[
                         T_{v-1}(d)<T_v(d)\le M.        \tag{3.5}
\]

If `T_u(d)=M`, choose `u`; otherwise choose any position in `[v,u]`
attaining `M`.  Let `R` be its maximal full-word component in the superlevel
set `{s:T_s(d)>=M}`.  Equation (3.5) prevents `R` from extending to the left
of `v`.

If `T_u(d)<M`, then `u` is outside `R`, so `R subseteq[v,u-1]`.  This is an
internal run and (3.4) follows.

It remains to take `T_u(d)=M`.  On the directed plateau `P'`, coordinate `d`
is one of three types.

- If it is strictly falling, then `T_(u+1)(d)<M`, so the component ends at
  `u` and (3.4) follows.
- If it is fixed, then the fixed level of `P'` is `M`, which is high
  absorption.
- If it is strictly rising, integer strictness gives
  \[
     T_{v'}(d)\ge M+\lambda(P')
       \ge(2x-1-2\epsilon)a>a,
  \]
  provided `epsilon<x-1`.  This contradicts `T_(v')(d)<=a`.

These cases exhaust a directed plateau.  The run is internal on the left by
(3.5) and on the right by the strict zero just identified.  QED.

### Why the earlier failure modes do not break Lemma 1

- **Partial later plateaux.**  In every cheap case the threshold component
  meets a strict zero no later than `u+1`; it cannot pass through a partial
  later plateau.  If it continues along `P'`, that is precisely the fixed,
  absorbing case.
- **Intermediate peaks.**  There may be many maxima or intermediate peaks in
  the complement gap.  Selecting any full component at the top level `M`
  keeps it inside `[v,u]`; no uniqueness of the maximum is required.
- **Shared endpoints.**  If `u=v`, the cheap component is the singleton
  `{v}` in the falling case and has cost zero.  The other cases are unchanged.
- **Word boundaries.**  Both selected plateaux are internal peaks.  Hence
  `v-1` and `u+1` exist.  Prefix and suffix gaps are never used.
- **Admissibility.**  A maximal component of `{T_s(d)>=M}` is exactly an
  admissible coordinate-threshold run in the definition used by
  `FABLE_RUN_SPECTRUM_AUDIT.md`.  Constancy is not required.

Thus the trace's concern about arbitrary superlevel components was resolved
in the favorable direction.  The local lemma was not the fatal point.

## 4. Capacity of the absorbing and long-gap alternatives

### Lemma 2 (high-line capacity)

Among regular seams, the number ending in high absorption is at most

\[
             3(3-2x+2\epsilon)a+O(1).                \tag{4.1}
\]

#### Proof

An absorbing successor has positive fixed level

\[
            t\ge(x-1-\epsilon)a.
\]

Its line must contain a regular plateau of edge length at least
`(x-epsilon)a`.  A coordinate line at level `t` has `2a-|t|` edges, so

\[
            t\le(2-x+\epsilon)a.
\]

There are at most `(3-2x+2epsilon)a+O(1)` integer levels in this interval
per direction.  Two regular plateaux cannot use the same line: each has more
than `a` edges, their edge sets are disjoint, and the whole line has at most
`2a` edges.  Summing over three directions proves (4.1).  QED.

Under the atom hypothesis, for every fixed `epsilon>0` all but `o(a)`
dangerous plateaux are regular, their number is `(2+o(1))a`, and their total
edge mass is `(2x+o(1))a^2`.  Therefore their vertex-complement gap mass is

\[
                    G=(3-2x+o(1))a^2.                \tag{4.2}
\]

The gaps are disjoint.  Hence the number of seams with `g>a` is at most

\[
                    (3-2x+o(1))a.                    \tag{4.3}
\]

Every exceptional plateau destroys at most two regular-to-regular seams.
Combining (4.1)--(4.3), the number of regular, nonabsorbing seams with
`g<=a` is at least

\[
 \big(8x-10-6\epsilon-o(1)\big)a.                   \tag{4.4}
\]

For `x>=4/3`, this is at least `(2/3-6epsilon-o(1))a`.

## 5. Exact modified first-dangerous assignment

The trace asserted that each cheap seam saves on `Theta(a)` starts, but did
not identify those starts.  The following interval is the missing object.

Take a nonabsorbing regular seam as in Lemma 1, with `g<=a`, and let
`R=[p,q] subseteq[v,u]` be its seam-local run.  Define

\[
 I_j=
 [\max\{u_-,v_j-L\},\,v-1]
       \cap[1,M_a-L].                                 \tag{5.1}
\]

### Lemma 3 (exact safe service interval)

Every `i in I_j` is assigned to `P_j` by the original first-dangerous rule,
and `R subseteq W_i`.  The intervals `I_j` belonging to distinct seams are
pairwise disjoint.  Before the global endpoint truncation,

\[
 |I_j|\ge
 \min\{\lambda_{j-1},L-\lambda_j-g-1\}.              \tag{5.2}
\]

Consequently, for a regular seam with `g<=a`,

\[
                         |I_j|\ge(x-\epsilon)a-O(1).  \tag{5.3}

#### Proof

The plateau `P_j` is complete in `W_i` exactly when

\[
                         v_j-L\le i\le u-1.          \tag{5.4}

For `i>=u_-`, neither `P_(j-1)` nor any earlier dangerous plateau can be
complete in `[i+1,i+L]`, because its start is at most `i`.  Thus (5.1) and
(5.4) make `P_j` the first complete dangerous plateau.

Also `i<=v-1<p`, while

\[
       i+L\ge v_j\ge u\ge q.
\]

Therefore `R subseteq W_i` and `R` avoids `i`.

The interval `I_j` lies in the edge-interior positions
`[u_(j-1),v_(j-1)-1]` of the predecessor plateau.  Those intervals are
disjoint for distinct predecessor plateaux, proving disjointness.

For a nonoverlapping seam, `u=v+g+1` and `v_j=u+lambda_j`, so the untruncated
integer interval has size

\[
 \min\{\lambda_{j-1},L-\lambda_j-g-1\}.
\]

A shared endpoint only increases the second quantity by one, so (5.2)
remains safe.  Finally, if `g<=a`, regularity and `x<=3/2` give

\[
 L-\lambda_j-g-1
   \ge(3-x-\epsilon)a+O(1)
   \ge(x-\epsilon)a+O(1),
\]

which proves (5.3).  Intersecting all disjoint intervals with the global
start range deletes only `O(a)` starts in total.  QED.

Reassign every `i in I_j` from `P_j` to `R`.  The new run is internal,
avoids `i`, and remains inside the same forward window, so the modified
assignment retains one-sided span and endpoint congestion at most `L+1`.
Reusing one run at `Theta(a)` starts is harmless: window containment, not a
seam-to-run multiplicity bound, is what proves the `O(a)` congestion in the
audited run-spectrum theorem.

The saving at one reassigned start is at least

\[
 \lambda_j-\lambda(R)
   \ge(x-1-\epsilon)a-O(1).                         \tag{5.5}
\]

Equations (4.4), (5.3), and (5.5) therefore give total saving

\[
 S\ge
 \Big((8x-10-6\epsilon)(x-\epsilon)(x-1-\epsilon)
       -o(1)\Big)a^3.                               \tag{5.6}
\]

This is the corrected `O(a^3)` arithmetic.  At `x=4/3`, its limiting
coefficient is

\[
                {2\over3}{4\over3}{1\over3}
                    ={8\over27}.                    \tag{5.7}
\]

The trace's intermediate `O(a^2)` saving statements counted seams but not
the `Theta(a)` service starts per seam; its larger unproved statements did
the reverse without establishing (5.1).  Formula (5.6) is the complete
ledger.

## 6. Contradiction with the capped-run lower bound

Choose `c=x-zeta`, where `zeta>0` is fixed and small.  Under the atom,

\[
 e_c={1\over a^2}\sum_j(\lambda_j-ca)
            \longrightarrow2\zeta.                 \tag{6.1}
\]

The audited first-dangerous theorem and its unconditional seam bound give

\[
 \begin{aligned}
 {Q_{\rm fd}\over a^3}
 &\le3c+2e_c+H_c+o(1),\\
 H_c&\le(4-c+o(1))e_c.
 \end{aligned}                                     \tag{6.2}
\]

Hence

\[
 {Q_{\rm fd}\over a^3}
 \le3x+(9-2x)\zeta+2\zeta^2+o(1).                  \tag{6.3}
\]

The modified assignment has exact cost

\[
                         Q_{\rm mod}=Q_{\rm fd}-S. \tag{6.4}
\]

At `epsilon=0`, define

\[
 S_0(x)=(8x-10)x(x-1).
\]

For `4/3<=x<=3/2`,

\[
 \begin{aligned}
 S_0(x)-(3x-4)
   &=8x^3-18x^2+7x+4\\
   &\ge {8\over27}>0.                               \tag{6.5}
 \end{aligned}
\]

Indeed its derivative `24x^2-36x+7` is positive throughout this interval,
so the minimum is attained at `x=4/3`.

Fix `epsilon>0` small enough that the coefficient in (5.6) still exceeds
`3x-4` by a positive constant.  Then choose `zeta>0` small enough that

\[
        (9-2x)\zeta+2\zeta^2
\]

is smaller than half that margin and `c=x-zeta>1`.  Equations
(5.6), (6.3), and (6.4) now give

\[
                         Q_{\rm mod}\le(4-\eta)a^3  \tag{6.6}
\]

for some fixed `eta>0` and all sufficiently large `a`.  This contradicts
the audited lower bound (2.1).  The atomic seam-exclusion theorem follows.

## 7. Stress-test ledger

| Potential failure | Audit result |
|---|---|
| Partial successor plateau enters the run | No.  A strict zero occurs at or before `u+1`, except in the explicitly absorbing fixed case. |
| Intermediate maxima or multiple peaks | Harmless.  A top-level component is still contained in the seam interval. |
| Shared plateau endpoint | Harmless; the cheap falling case gives a singleton run, and the service count loses at most one. |
| Prefix/suffix boundary escape | Not used.  Selected peaks are internal and only predecessor-successor seams are charged. |
| Arbitrary superlevel component is not an admissible run | False concern.  The audited definition allows every maximal coordinate-threshold component. |
| One seam run is assigned to many starts | Harmless.  All assignments lie in length-`L` forward windows, which gives congestion `L+1` automatically. |
| Service intervals from different seams overlap | They do not: each lies in the edge interior of a distinct predecessor plateau. |
| A start was not originally assigned to the successor | Fixed by the exact lower endpoint `max{u_(j-1),v_j-L}` in (5.1). |
| The run is outside the start's window | Fixed by `i<=v-1` and `i>=v_j-L`, since `R subseteq[v,u] subseteq[v,v_j]`. |
| Final `L` omitted starts destroy cubic saving | They delete only `O(a)` starts from disjoint service intervals, costing `O(a^2)`. |
| Long gaps dominate | Their count is at most `(3-2x+o(1))a`; the remaining positive-density seams yield (5.6). |
| `O(a^3)` saving was double-counted | No.  There are `Theta(a)` disjoint cheap seams, `Theta(a)` disjoint starts per seam, and `Theta(a)` saving per start. |

## 8. Final theorem ledger

### Proved here, conditional on the inherited audited framework

1. The seam-local maximum trichotomy, Lemma 1.
2. The high-absorption line-capacity bound, Lemma 2.
3. The exact safe first-dangerous service interval, Lemma 3.
4. A modified span-`4a+3` run assignment with the cubic saving (5.6).
5. Exclusion of every atomic profile `2 delta_x` for
   `4/3<=x<=3/2` when `D=o(a^2)`.

### Not proved

1. Exclusion of a non-atomic or mixed limiting plateau profile.
2. A stability theorem reducing arbitrary survivors to one atom.
3. A universal strict-sub-four run assignment for every middle order.
4. The three-box impossibility theorem.
5. Any new exact value or asymptotic formula for the original OR problem.

The correct conclusion is therefore neither “the trace was wholly wrong” nor
“the general problem is solved.”  Its local maximum idea was valid, its
published charging argument was incomplete, and the exact interval (5.1)
repairs that gap strongly enough to eliminate the balanced atomic survivor.
