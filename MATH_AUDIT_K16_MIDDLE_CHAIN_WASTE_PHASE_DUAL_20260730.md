# K16 middle-chain waste: exact identities, a ghost exclusion, and the missing physical dual

**Date:** 2026-07-30  
**Status:** proved identities and scoped countermodels; no global `12873` no-go

## 1. Verdict

The first-middle inventory is a useful exact coordinate system, but its
``waste`` identity is a partition identity rather than a new lower bound.  For
a universal word it says

\[
   L-W=S+J+F+G,
\]

where the four terms are stalls, jumps, flat extras, and ghost extras.  Thus
proving waste at least four for K16 is exactly the still-open assertion
`L>=12874`, not a consequence of the definition.

The audit does prove one new global restriction.  It uses neither a doubled
parent nor a flat carrier:

> **Any universal K16 word of length 12,873 has no ghost extra.**

Consequently every such word would satisfy

\[
   G=0,\qquad S+J+F=3.
\]

The bit-phase loss identity is also valid after an important correction.  A
coordinatewise equation in which every bit is exactly at its `6435` demand
must include the extra-incidence vector contributed by repeated deliveries.
For the authenticated length-12,874 word this vector is

```text
(0,3,4,3,2,0,0,4,4,1,1,1,4,4,0,1),
```

with sum `32=8*4`.  Only bits `0,5,6,14` are exactly tight.  The other twelve
coordinates have one to four extra bit-free delivery occurrences.  Hence the
uncorrected claim `loss_x=gapcap_x-6435` for every bit is false on the very
word used to motivate it.

Finally, a solver-free finite construction gives a waste-three **abstract
column system** which covers every actual lower and middle K16 subset with
the right containments and depth.  It is not one physical contiguous-OR word:
it deliberately omits overlap compatibility between adjacent columns.  This
pinpoints the missing ingredient.  No dual based only on monotone deadlines,
depth three, within-column nesting, and layer counts can prove the desired
fourth unit.

The exact bracket therefore remains

\[
   12873\leq \nu(16)\leq12874.
\]

## 2. Definitions

Let `A=(A_0,...,A_(L-1))` be a word of nonempty subsets of `[k]`, and write

\[
  U(p,q)=\bigcup_{i=p}^q A_i,
  \qquad r=\lceil k/2\rceil,
  \qquad W=\binom{k}{r}.
\]

For a left endpoint `p`, let

\[
  \tau_p=\min\{q\geq p: |U(p,q)|\geq r\},
\]

when this set is nonempty.

* `p` is a **stall** if `tau_p` does not exist.
* `p` is a **jump** if `tau_p` exists and `|U(p,tau_p)|>r`.
* `p` is a **delivery** if `|U(p,tau_p)|=r`.  Its **deadline** is
  `q_p=tau_p` and its delivered middle target is `T_p=U(p,q_p)`.

For one target `T`, group all its delivery occurrences by their deadline.
If the group at `q` has multiplicity `m(T,q)`, define

\[
  F=\sum_{T,q}(m(T,q)-1)
\]

to be the number of **flat extras**.  Define

\[
  G=\sum_T\bigl(|\{q:m(T,q)>0\}|-1\bigr)
\]

to be the number of **ghost extras**.  Thus a flat repeats a target at the
same deadline, while a ghost repeats it at a different deadline.  Let `S,J`
denote the numbers of stalls and jumps.

This first-delivery waste must not be conflated with either of the following:

1. the compiler short-cell slack `dL-binomial(d,2)-Lambda`; or
2. the number of middle intervals unchanged by deleting one endpoint.

For K16 upper12874 the three numbers happen to be `4`, `12287`, and `4`.
For the optimal K14 word they are `2`, `392`, and `1`, so they are genuinely
different statistics.

## 3. Exact first-delivery identities

### Theorem 3.1 (inventory partition)

Let `M` be the number of distinct delivered middle targets and let
`H=W-M`.  Then every nonzero word satisfies

\[
  \boxed{L=(W-H)+S+J+F+G.} \tag{3.1}
\]

In particular, if the word is universal, then `H=0` and

\[
  \boxed{L-W=S+J+F+G.} \tag{3.2}
\]

**Proof.**  Every left endpoint is exactly one stall, jump, or delivery.  If
`D` is the number of deliveries, the deadline groups for one target contribute
one first occurrence, `F` further occurrences within groups, and `G` first
occurrences of later groups.  Hence `D=M+F+G`, while `L=D+S+J`.  Substitution
gives (3.1).  Universal coverage gives `M=W`.  QED.

### Lemma 3.2 (global deadline monotonicity)

If `p<p'` are delivery endpoints, then `q_p<=q_(p')`.  If their deadlines are
equal, their delivered targets are equal.

**Proof.**  If `q_(p')<q_p`, then

\[
 U(p',q_{p'})\subseteq U(p,q_p).
\]

Both sides have rank `r`, so they are equal.  It follows that `U(p,q_(p'))`
already has rank `r`, contradicting the minimality of `q_p`.  Equality of the
deadlines gives nested rank-`r` sets and hence equal targets.  QED.

This statement holds across stalls and jumps; it need not be restricted to a
stall-free or jump-free stretch.

### Lemma 3.3 (deadline-hole span bound)

Let `Q` be the set of distinct delivery deadlines.  Every delivery satisfies

\[
  q_p-p\leq L-|Q|. \tag{3.3}
\]

If the word is universal and `e=L-W`, then `|Q|=W+G` and therefore

\[
  q_p-p\leq e-G. \tag{3.4}
\]

**Proof.**  List `Q` as `v_1<...<v_|Q|`.  At most `L-|Q|` integer deadlines
are absent, so `v_j<=j-1+L-|Q|`.  A delivery in the `j`th group has at least
one endpoint from each earlier group before it, hence `p>=j-1`.  This proves
(3.3).  In a universal word every one of the `W` targets has one deadline
group and the ghosts are precisely its additional groups, so `|Q|=W+G`.
QED.

### Lemma 3.4 (one terminal waste unit)

For `r>1`, every universal word has at least one first-delivery waste unit.

**Proof.**  Universality forces a singleton letter, so not every letter has
rank `r`.  If the final letter has rank below `r`, its endpoint stalls; if it
has rank above `r`, it jumps.  Otherwise take the maximal terminal run of
rank-`r` letters and inspect its predecessor.  A predecessor of rank above
`r` jumps.  A predecessor of rank below `r`, after adjoining the next
rank-`r` letter, either jumps above `r` or delivers the same target as that
next endpoint.  The latter is a flat extra.  QED.

Applying the same argument after reversal gives a terminal unit in the
reverse inventory.  The two conclusions are not additive; the universal K4
word with `L-W=1` is already a counterexample to adding them.

## 4. A global K16 theorem: a 12,873 candidate is ghost-free

Put

\[
  \Lambda=\sum_{s=1}^{r-1}\binom{k}{s}.
\]

For a column `p`, let `f_p` be the number of its initial interval cells of
rank below `r`: it is `q_p-p` for a delivery or jump, and `L-p` for a stall.
Every lower target must occur in one of these cells, so

\[
  \Lambda\leq\sum_p f_p. \tag{4.1}
\]

The monotone-deadline depth lemma gives `f_p<=e=L-W` for every column in a
universal word.  Lemma 3.3 improves this to `f_p<=e-G` on delivery columns.
Let `N=S+J`.  From (3.2),

\[
  N+F=e-G,
\]

so in particular `N<=e-G`.  There are `L-N` delivery columns and `N`
nondelivery columns.  Therefore

\[
\begin{aligned}
  \Lambda
  &\leq (L-N)(e-G)+Ne\\
  &=L(e-G)+NG\\
  &\leq (e-G)(L+G).                         \tag{4.2}
\end{aligned}
\]

For a hypothetical universal K16 word of length `L=12873`,

\[
  W=12870,\qquad e=3,\qquad \Lambda=26332.
\]

If `G=1`, the right side of (4.2) is only

\[
  2(12873+1)=25748<26332.
\]

For `G=2` or `3` it is smaller still.  Hence `G=0`.  This proves the stated
ghost exclusion without any construction hypothesis.

Reversal preserves universality and length, so the same argument also gives
`G_rev=0` for the first-middle inventory scanned from right to left.

The exact surviving inventory cases are

```text
S+J = 0,1,2,3
F   = 3,2,1,0
G   = 0.
```

This theorem kills the long-range-ghost pattern of the known one-hole word,
but it does not kill a different physical word with three flats, or with one
to three nondeliveries.

The rank-slack equality audit does not supply the missing step.  At the K16
lower-bound length its slack is

\[
  \sigma=3W+\binom42-\Lambda=12284>0.
\]

Only zero slack forces a flat middle row and bijective lower band.  Therefore
neither a flat carrier nor the observed two-rail phase arrangement may be
assumed for a hypothetical length-12,873 word.

## 5. Correct bit-phase accounting

Assume now that `k=2r` and the word is universal.  For a coordinate `x`, let

\[
  c_x=|\{p:x\notin A_p\}|.
\]

Call such an endpoint **lost for x** if it stalls or jumps, or if it delivers
a target containing `x`.  Let `ell_x` be the number of lost endpoints and let

\[
  D_x=|\{p:p\text{ delivers and }x\notin T_p\}|.
\]

Then, directly from the definitions,

\[
  c_x=\ell_x+D_x.                            \tag{5.1}
\]

Exactly

\[
  \binom{2r-1}{r}=W/2
\]

middle targets omit `x`.  Put

\[
  E_x=D_x-W/2\geq0.
\]

The corrected coordinate equation is

\[
  \boxed{\ell_x=c_x-W/2-E_x.}                \tag{5.2}
\]

Every duplicate delivery occurrence omits exactly `r` coordinates.  Hence

\[
  \boxed{\sum_xE_x=r(F+G).}                  \tag{5.3}
\]

Also, summing (5.1) and using `D=L-S-J`,

\[
  \boxed{
  \sum_x\ell_x=rL-\sum_p|A_p|+r(S+J).
  }                                           \tag{5.4}

Equation (5.4) is the valid loss-sum identity.  Arrangement affects the
coordinate distribution, not its total once the letter ranks and number of
nondeliveries are fixed.

For `answers/k16_upper12874.word`, the exact values are

```text
sum_p |A_p| = 65036
S=J=0
sum_x ell_x = 8*12874-65036 = 37956
E = (0,3,4,3,2,0,0,4,4,1,1,1,4,4,0,1)
sum_x E_x = 32 = 8*(3 flats + 1 ghost).
```

Thus `37956`, not `37968`, is the value of the displayed loss-sum formula on
this word.  Moreover `ell_x=c_x-6435` holds only when `E_x=0`, namely for
bits `0,5,6,14`.  A phase-gap dual may still be possible, but it must retain
the nonnegative, quantized vector `E`.

For a hypothetical length-12,873 word, Section 4 gives `G=0`; therefore
`sum_x E_x=8F`.  The four surviving inventory cases have total extra
bit-free incidence `24,16,8,0`, respectively.

## 6. Exact retained-word census

The first-delivery audit gives:

| word | `d` | `L-W` | `S` | `J` | `F` | `G` | middle holes |
|---|---:|---:|---:|---:|---:|---:|---:|
| K10 optimum | 2 | 2 | 1 | 0 | 1 | 0 | 0 |
| K12 optimum | 2 | 2 | 1 | 0 | 1 | 0 | 0 |
| K14 optimum | 2 | 2 | 1 | 0 | 1 | 0 | 0 |
| K16 upper12874 | 3 | 4 | 0 | 0 | 3 | 1 | 0 |
| K16 authenticated item-1995 H1 source | 3 | 3 | 1 | 0 | 2 | 1 | 1 |

The four K16 extras are exactly three same-deadline flats and one
different-deadline ghost.  The long-range duplicate `0xc279` is the ghost.
For the authenticated 12,873-cell source of handoff item 1995, the exact
inventory is one stall, two flats, one ghost, and one middle hole.  Thus the
ledger description of that source as stall-free with the same three flats as
upper12874 is stale; the waste-four conclusion survives, but its partition
does not.
The earlier optimal K4, K6, and K8 words have first-delivery waste `1,1,2`
at depths `1,1,2`.  Thus all proved even optima through K14 merely realize
the rank-slack budget `d`; the K16 value four belongs to an upper certificate,
not to a proved optimum.

An independent census of **all** middle intervals finds one additional
same-start containment event at the head.  It is not an additional
first-delivery occurrence, because one left endpoint contributes only its
first crossing.  That census also proves a scoped negative result for the
proposed elementary endpoint signature:

* the optimal K14 word has only one elementary boundary event although
  `2^(d-1)=2`; and
* the four K16 event signatures are not canonically saturated (`01,00,01,11`
  for cumulative containment and `11,10,11,10` for incremental gain).

This refutes that elementary-event/signature theorem.  It does **not** refute
a different theorem about total first-delivery waste.

## 7. Countermodels to signature-only proofs

### 7.1 A physical middle-only word with waste three

List every rank-eight K16 set once as a one-cell letter, in any order, and
append three copies of one singleton.  The first `W` endpoints deliver all
middle targets immediately and distinctly; the last three endpoints stall.
Thus

\[
  S=3,\quad J=F=G=0,
\]

and the physical nonzero word has first-delivery waste three.  It is not
universal below the middle layer.  Therefore middle coverage, nonzeroness,
deadline monotonicity, terminal waste, and the bit-sum identities alone
cannot force waste four.

### 7.2 An abstract cover of every actual lower and middle target

The finite audit constructs containment injections

\[
\begin{array}{rcl}
 \binom{[16]}1\cup\cdots\cup\binom{[16]}5 &\hookrightarrow& \binom{[16]}6,
       \qquad 6884\to8008,\\
 \binom{[16]}6 &\hookrightarrow& \binom{[16]}7,
       \qquad 8008\to11440,\\
 \binom{[16]}7 &\hookrightarrow& \binom{[16]}8,
       \qquad 11440\to12870.
\end{array}
\]

Tracing inverse images from each rank-eight set partitions all lower targets
into nested columns containing at most three lower sets and one unique middle
set.  The exact lower-count histogram is

```text
0 lower targets: 1430 columns
1 lower target : 3432 columns
2 lower targets: 1124 columns
3 lower targets: 6884 columns
```

and

```text
0*1430 + 1*3432 + 2*1124 + 3*6884 = 26332 = Lambda.
```

Put these `W` columns on the deadline staircase `q(p)=p+3`.  Two boundary
closures give abstract waste three:

1. keep the final three endpoints as stalls (`S=3,F=0`); or
2. let all endpoints deliver and collapse the final four endpoints onto the
   last deadline (`S=0,F=3`).

Both systems have monotone deadlines, depth at most three, all `W` real
middle targets, all `Lambda` real lower targets, correct containment inside
every representative column, and no ghost.

They are not physical words.  They do not enforce the simultaneous overlap
relations

\[
 U(p,q)=A_p\cup U(p+1,q)=U(p,q-1)\cup A_q.   \tag{7.1}
\]

Thus (7.1), or an equally strong seam/overlap invariant derived from it, is
exactly what a valid global fourth-waste proof must use.  The scalar deadline
LP and independent-column containment relaxation have optimum three.

## 8. Doubling arithmetic and extrapolation scope

For the odd K15 optimum, `W=6435`, `d=3`, and `L=W+d=6438`.  Literal even
doubling with a singleton bridge has length

\[
  2(W+d)+1=12877.
\]

The K16 lower-bound target is

\[
  2W+d=12873.
\]

Therefore a literal doubled construction must save `d+1=4` cells.  The
authenticated length-12,874 word saves only three.  A statement that the
singleton bridge cannot merge with all three parent waste states would
explain the remaining unit **within that architecture**.  No argument here
promotes it to arbitrary words, and no doubled-parent, one-run, two-rail, or
flat-carrier normal form is known globally.

The small even data also do not select a general law.  For deadline depths
`d=1,2,3`, both

\[
  2^{d-1}
  \quad\hbox{and}\quad
  2^{\lceil\log_2 d\rceil}
\]

give `1,2,4`.  The even deadline depth first becomes `1,2,3,4,5` at
`k=4,8,16,32,52`, respectively.  At `d=4` the two proposals already diverge
(`8` versus `4`).  Exponential-in-`d` waste has no proved structural
injection and should not be extrapolated from K16.  At K16 the exact question
is only whether depth three forces one extra unit beyond the rank-slack
budget.

## 9. Exact-frontier scope and frozen audit

The current exact-search frontier is consistent with this scope.  Item 1995
of `MATHEMATICAL_HANDOFF.md` excludes radius-three substitutions of one fixed
12,873-cell source.  Item 1997a excludes one substitution after a deletion
and arbitrary cut only for bases having at most five holes.  Item 1996
explicitly stops at a scalar phase trace because the physical generalized
braid remains unproved.  None of these results gives a global normal form for
an arbitrary length-12,873 word, so none can be used to promote the scoped
doubling or phase signatures above into a theorem.

The solver-free checker is

```text
scratch/audit_k16_middle_chain_phase_dual_20260730.py
SHA-256 899b3542e5ac088508a0c0db20fb43aad3a37e5780f6c63dde0e1e3c1ba1b812
```

and emits

```text
scratch/k16_middle_chain_phase_dual_20260730.audit.json
SHA-256 37aae14f5bc3dd06db7bd545ec1ade588ce2d18ce11a3b0949eaaaf51cb5f76c
payload 1d3be70a20922e7c5ff9218215353ee5af88300a83071b605b55df9bcf51eab1
```

The input hashes are reauthenticated in the JSON.  The three deterministic
containment-matching hashes are also recorded there.  Re-execution reproduces
the JSON byte for byte.  The canonical words were independently replayed by
the existing exact OR verifier and cover all `2^k-1` nonzero masks.

The elementary-event counterexample used in Section 6 is separately frozen
in

```text
THREAD_D_EVEN_DEPTH_BOUNDARY_SIGNATURE_COUNTEREXAMPLE_20260730.md
scratch/threadD_even_depth_boundary_signature_counterexample_20260730.audit.json
```

No claim in this note proves `nu(16)=12874` or supplies a length-12,873
universal word.
