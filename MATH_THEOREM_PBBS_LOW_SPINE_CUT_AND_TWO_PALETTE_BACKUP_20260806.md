# Cutting the low PBBS spine and restoring its two immediate palettes

**Date:** 2026-08-06  
**Method:** explicit PBBS height-spine calculus, two independent Johnson
backup edges, missing-tag separation, and tagged component chaining; no
computation or finite search  
**Status:** unconditional prospective owner/`q1` construction.  Deleting all
role-zero height-spine edges removes the linear residence obstruction and
allows an incoming collar at every pentagon tail.  Every deleted edge's
lower and upper immediate colours are restored by two fresh isolated backup
edges.  The resulting polynomial protected bank is a path forest and may be
joined into one oriented protected path.  The theorem does not transport
the five-role lower source occurrence bijection or prove arbitrary-width
upper completeness or typed-cap acceptance.

## 1. The direct height spine is not a resident source host

Use the notation

\[
 A_h=0\,1^h0^h(10)^{r-h},
 \qquad U_h=\Omega\setminus A_h,
 \qquad R=r+1.
\tag{1.1}
\]

The role-zero rethread edge at height `h` is

\[
 e_h=U_hU_{h+1},
 \qquad
 U_{h+1}=U_h-\{h+1\}+\{2h+1\}.
\tag{1.2}
\]

The coordinate `2h+1` enters on `e_h` and leaves on `e_(2h)`.  Whenever
both edges lie in the retained spine interval, its positive run on that
spine has `h` owners.  In particular every

\[
 4\le h\le\min\{\delta,\lfloor(H-1)/2\rfloor\}
\]

is a depth-`delta` residence violation in a spine retained through height
`H-1`.  Thus in the deadline-scale regime `H=Theta(delta)` there are
`Theta(delta)` fixed owner-run defects.  No choice of a source antecedent or
of event order on other edges can repair these runs.

This also explains the failed common-history pinning at low heights: an
internal source letter for the edge `e_h` lies in the intersection of
`delta+1` consecutive spine owners, while some of its forced event labels
have already left that intersection.

## 2. Exact palettes of one deleted edge

Put

\[
 L_h=U_h\cap U_{h+1},
 \qquad
 T_h=U_h\cup U_{h+1}.
\tag{2.1}
\]

Then `|L_h|=R-1`, `|T_h|=R+1`, and `e_h` has lower immediate colour `L_h`
and upper immediate colour `T_h`.  Explicitly,

\[
 L_h=\{0,h+2,\ldots,2h,2h+2,2h+4,\ldots,2r\},
\tag{2.2}
\]

while `T_h` has least positive element `h+1`.  Thus both families
`(L_h)_h` and `(T_h)_h` are pairwise distinct.

### Lemma 2.1 (separate palette backups)

For each deleted edge `e_h`, choose distinct `a_h,b_h outside L_h` and
distinct `c_h,d_h in T_h`.  The two Johnson edges

\[
 f_h^-=(L_h+a_h)(L_h+b_h),
\tag{2.3}
\]

and

\[
 f_h^+=(T_h-c_h)(T_h-d_h)
\tag{2.4}
\]

have respectively

\[
 (L_h+a_h)\cap(L_h+b_h)=L_h,
 \qquad
 (T_h-c_h)\cup(T_h-d_h)=T_h.
\tag{2.5}
\]

So `f_h^-` restores the omitted lower colour and `f_h^+` restores the
omitted upper colour.  No single fresh edge can restore both: the two
rank-`R` subsets of the fixed interval `[L_h,T_h]` giving both palettes are
exactly `U_h,U_(h+1)`.

## 3. Simultaneous fresh choice

Let `H=O(sqrt R)` and delete all high role-zero edges in the selected
height interval.  The backup edges (2.3)--(2.4) can be chosen simultaneously
so that all their owners and lower facets are distinct and avoid every
pentagon owner/facet not belonging to a deleted edge.

Indeed, `Omega-L_h` has `R` elements.  A previously reserved owner rules out
at most one choice of `a` or `b`, while the facet of (2.3) is the new,
pairwise distinct set `L_h`.  Thus after `O(H)` reservations there remain
`R-O(H)` eligible outside elements.

For (2.4), there are `R+1` possible owners `T_h-c`.  A reserved owner rules
out at most one `c`, and a reserved rank-`(R-1)` facet rules out at most one
unordered pair `{c,d}`.  Again `R-O(H)` individual choices and
`Theta(R^2)` pairs remain.

Use the global PBBS tag reservoir before making these choices.  Every
`L_h,T_h` contains all global tags.  Choose `a_h,b_h,c_h,d_h` to be
non-tags.  Then every backup owner and facet contains every global tag,
whereas every positive-time collar/arm interior misses its private tag.
Consequently the later missing-tag collar construction cannot collide with
the backups.  Only the `O(H)` all-tag pentagon endpoints need be excluded,
which is already covered by the preceding count.

### Theorem 3.1 (all-tail-collar protected forest)

Delete every role-zero rethread edge `e_h`.  Retain the four rethread edges
at roles `1,2,3,4`.  Put one incoming synchronized collar at **all five**
tails `P_(h,i)`, including `P_(h,0)=U_h`, and add the two backup edges
`f_h^-,f_h^+`.

For a prospective missing-tag choice, the resulting protected incidence
bank is a path forest on both the owner and lower-facet shores.

#### Proof

The only cross-height tail/head identity in the high PBBS bank is

\[
 P_{h,0}=Q_{h-1,1}=U_h.
\]

But `Q_(h-1,1)` was incident only through the now deleted role-zero edge.
Thus `U_h` receives its incoming collar and no pentagon edge, so its
protected degree is one.  Every other tail receives one collar edge and
one retained rethread edge, so its degree is two.  No other tail/head
identity occurs.  Private missing tags separate collar interiors, and
Section 3 separates every backup resource.  The backup edges are isolated.
Therefore every protected component is a path. \(\square\)

## 4. Size, exposure, and component debt

There are `O(H)` collared pentagon pieces and `2O(H)` isolated backup
edges.  The collars use `O(HR)` transitions and exposure `O(H)`.  The
backups change these bounds only by `O(H)`.

Give every free endpoint a private one-tag arm of length `floor(R/4)` and
join the resulting far ports using pair-tag connectors.  The tagged-chain
theorem applies to the `O(H)` protected components.  Hence, for
`H=O(sqrt R)`, the complete forced bank has

\[
 e=O(HR)=O(R^{3/2}),
 \qquad
 \alpha,\beta=O(H)=O(\sqrt R),
\tag{4.1}
\]

and is one oriented protected path.  The protected component debt is
therefore one, not `Theta(H)`.  A polynomial protected-factor extension
then contains this path in a simple spanning two-factor; as usual, extra
unprotected factor cycles may remain.

The long arms also remove the *owner-level* low-spine residence obstruction:
each isolated backup edge can be treated as a one-edge fixed block between
two long arms, and every retained collared piece has a long arm at its free
end.  The exact two-sided aperture theorem schedules their external flags.
This statement is conditional only on a literal history for the fixed
collar/rethread block itself.

## 5. Exact palette ledger

At immediate depth, the construction is lossless:

1. roles `1,2,3,4` retain their original lower and upper colours;
2. for every omitted role-zero edge, `f_h^-` supplies exactly its old lower
   colour `L_h`;
3. for every omitted role-zero edge, `f_h^+` supplies exactly its old upper
   colour `T_h`; and
4. all added collar, arm, connector, and backup lower facets are distinct,
   so no protected lower-capacity conflict is hidden.

This is a coverage ledger, not a claim that (2.3) and (2.4) occupy the old
physical occurrence address.

## 6. Exact remaining scope

The theorem is deliberately graph-level.  Cutting the spine changes the
five-head occurrence permutation.  Therefore it does **not** yet prove:

1. the five-role common-history occurrence bijection for the strict-lower
   compiler;
2. arbitrary-width upper preservation after opening role zero;
3. a literal depth-`delta` antecedent simultaneously carrying the collared
   pieces and the palette backups;
4. occurrence-labelled typed-cap acceptance; or
5. fusion of the unprotected completion cycles.

The next local theorem must replace the missing fifth common-history role
by a source-occurrence router through the two palette backups (or by an
open four-role transport with bounded, regenerating deficiency).  Immediate
palette counts and low-spine residence are no longer obstructions on this
cut face.
