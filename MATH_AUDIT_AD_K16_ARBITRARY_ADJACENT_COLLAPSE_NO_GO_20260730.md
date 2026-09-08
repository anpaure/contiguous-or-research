# AD audit: no arbitrary adjacent two-to-one collapse of the authenticated K16 word

Date: 2026-07-30

## 1. Audited objects

The authenticated literal word is

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
length  12874
```

The audited exhaustive driver is

```text
scratch/audit_ad_k16_upper12874_arbitrary_adjacent_collapse_20260730.py
SHA-256 3e301c901df6112578c879f5af86dfb62eb6fb6b7619588382c1b750c7f72da8
```

Its H100-CPU result and execution records are

```text
scratch/k16_upper12874_arbitrary_adjacent_collapse_20260730.audit.json
SHA-256 f38f4a7ce7ad1dd0f518850b0d241a60e5cb5606826c01b2a51b72ed1c94d180
payload  8b5c1acb8f84a822a1f88b549fe78c777bf38527eb9e5e9c11ea412cdfed1e47

scratch/k16_upper12874_arbitrary_adjacent_collapse_20260730.stdout
SHA-256 78a3c340d107ccc1820d788b415c7de4a3c82d1e0a306ac7a3c1d07b6aa8dd60

scratch/k16_upper12874_arbitrary_adjacent_collapse_20260730.exit
SHA-256 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa

scratch/k16_upper12874_arbitrary_adjacent_collapse_20260730.resource
SHA-256 a181d775757cdcade75a60c3cf5e16e3fe33cb860a9b036e2f3ec65405120e7a
```

The stdout reports `12873` boundaries, zero hits, and status
`PASS_EXHAUSTIVE_NO_ARBITRARY_ADJACENT_COLLAPSE`.  The exit record is `0`.
The remote execution took 1.02 seconds wall time, used one CPU, and had peak
resident memory 52,224 KiB.  The driver itself fails closed unless its host
short name is `arboghast` and the word hash and length equal the values above.

## 2. Exact source-relative theorem

### Theorem 2.1

Let

\[
                 W=(w_0,w_1,\ldots,w_{12873})
\]

be the exact authenticated word above.  For every integer
\(p\in\{0,1,\ldots,12872\}\) and every nonzero 16-bit mask
\(y\in\{1,\ldots,65535\}\), the length-12873 word

\[
 W_{p,y}=(w_0,\ldots,w_{p-1},y,w_{p+2},\ldots,w_{12873})
\]

is not a universal contiguous-OR word on the nonzero 16-bit masks.

This theorem is strictly source-relative.  It does not rule out a deletion
plus a nonadjacent edit, an adjacent collapse accompanied by any other edit,
a permutation or rethreading of the remaining cells, or any unrelated
length-12873 word.

## 3. Collapse criterion

Fix a universal word \(w=(w_0,\ldots,w_{n-1})\) and a boundary
\(0\leq p\leq n-2\).  The two cells \(w_p,w_{p+1}\) are to be replaced by one
nonzero cell \(y\).  For a target \(T\), let

* \(f(T)\) be the least ending index of an old interval whose OR is \(T\);
* \(\ell(T)\) be the greatest starting index of an old interval whose OR is
  \(T\).

The target has an unchanged witness wholly in the left outside word exactly
when \(f(T)\leq p-1\), and it has one wholly in the right outside word exactly
when \(\ell(T)\geq p+2\).  Thus the exact critical set is

\[
 {cal C}_p=\{T:f(T)\geq p\text{ and }\ell(T)\leq p+1\}.       \tag{3.1}
\]

Let \(L_p\) be the ORs of all suffixes of
\((w_0,\ldots,w_{p-1})\), including the empty suffix, and let \(R_p\) be the
ORs of all prefixes of \((w_{p+2},\ldots,w_{n-1})\), including the empty
prefix.  Put

\[
 B_p=\{a\mathbin\vee b:a\in L_p,\ b\in R_p\},\qquad
 K_p=\bigcap_{T\in{cal C}_p}T,                              \tag{3.2}
\]

where the intersection of an empty family is the full mask.

### Lemma 3.1 (exact maximal-intersection criterion)

There is a nonzero replacement \(y\) covering every critical target if and
only if \(K_p\neq0\) and, for every \(T\in{cal C}_p\), there is an
\(s\in B_p\) such that

\[
                 T\mathbin\&\neg K_p\ \subseteq\ s\ \subseteq\ T.       \tag{3.3}
\]

When (3.3) holds, choose one such \(s_T\) for every critical target and set

\[
                   y=\bigvee_{T\in{cal C}_p}(T\mathbin\&\neg s_T).     \tag{3.4}
\]

If (3.4) is zero, replace it by any singleton bit of \(K_p\).  This gives a
literal valid replacement.

#### Proof

Every new interval containing \(y\) consists of a suffix of the left outside
word, then \(y\), then a prefix of the right outside word.  Its OR is therefore
\(s\vee y\) for some \(s\in B_p\); conversely every such choice is realized by
a literal interval.  Every interval avoiding \(y\) is an unchanged interval
wholly in one outside segment.  Hence only the targets in (3.1) need a new
witness.

If \(y\) works, then \(y\subseteq T\) for every critical target, so
\(0<y\subseteq K_p\).  If \(s\vee y=T\), then \(s\subseteq T\), while every
bit of \(T\) outside \(K_p\), and hence outside \(y\), must belong to \(s\).
This proves necessity of (3.3).

Conversely, choose the \(s_T\)'s in (3.3).  Each deficit
\(T\mathbin\&\neg s_T\) is a submask of \(K_p\), so (3.4) is a submask of
\(K_p\), hence of every critical target.  It contains the whole deficit of
each target, and therefore \(s_T\vee y=T\).  If all deficits vanish, adding
one bit of the nonzero \(K_p\) stays inside every target and preserves these
equalities.  Thus the constructed \(y\) is nonzero and works literally.  This
proves sufficiency. \(\square\)

The lemma eliminates an explicit loop over all 65,535 possible replacement
values without relaxing the problem.

## 4. Index and sweep audit

The driver computes the distinct ORs of nonempty intervals ending at each
old position and starting at each old position.  These tables give \(f\) and
\(\ell\) exactly.  Its endpoint conventions agree with (3.1)--(3.2):

* at `p=0`, the left-side list is exactly `(0,)`;
* at `p=n-2`, the right-side list is exactly `(0,)`;
* otherwise the left list is zero plus the ending-OR row at `p-1`, and the
  right list is zero plus the starting-OR row at `p+2`.

At `p=0`, (3.1) reduces to \(\ell(T)\leq1\), since every old witness has
\(f(T)\geq0\).  If

\[
 {cal C}_p=\{T:f(T)\geq p,\ \ell(T)\leq p+1\},
\]

then moving to `p+1` first removes precisely the bucket \(f(T)=p\), and then
adds precisely the bucket \(\ell(T)=p+2\) subject to \(f(T)\geq p+1\).  This
is exactly the update implemented by the driver.  There is no missing first
or last boundary and no `p+1`/`p+2` error.

As a solver-free regression, I exhaustively compared the criterion with
direct replacement enumeration for every universal length-four word over
the seven nonzero 3-bit masks.  There are 18 such words and 54 adjacent
boundaries.  The incremental critical set equalled its direct definition at
every boundary, and the criterion agreed with literal brute force in all 54
cases.

## 5. Artifact audit and result

The JSON contains one row for each consecutive position `0,...,12872`.
Its stable payload hash was independently recomputed after removing the
`payload_sha256` field and equals the claimed value.  Across all rows I also
checked, without rerunning the census, that:

* source left/right values agree with the authenticated word;
* every critical-target list is sorted and duplicate-free;
* `critical_count` equals its list length;
* the bitwise intersection of the listed targets equals the stored
  `intersection`;
* a `FAIL_ZERO_INTERSECTION` row has intersection zero;
* a `FAIL_SIDE_BASE` row has nonzero intersection, its `failed_target` is a
  listed critical target, and `required_from_side` equals
  `failed_target & ~intersection`;
* the stored failure and critical-count histograms are reproduced exactly;
* `hit_count=0` and the hit list is empty.

Independent source reconstruction at positions `0`, `1`, `88`, `6436`, and
`12872` reproduced the exact critical lists and side-base counts.  It also
replayed the stored side-base failure at the two endpoints and the interior
sample, and the zero-intersection failures at positions `88` and `6436`.
These samples explicitly exercise the empty-left, empty-right, ordinary
interior, and both failure branches.

The exact failure histogram is

```text
FAIL_SIDE_BASE          12834
FAIL_ZERO_INTERSECTION     39
total boundaries        12873
PASS                         0
```

The exact critical-count histogram is

```text
count  boundaries
  3         1
  5         1
  6         2
  8         2
  9         1
 10        32
 11       194
 12       382
 13       669
 14      1146
 15      1620
 16      1776
 17      1685
 18      1685
 19      1330
 20       899
 21       643
 22       360
 23       337
 24        80
 25        28
```

The largest ending-OR row has 11 states, the largest starting-OR row has 12
states, and the largest realized side-base set has 54 states.  Thus every
row terminates in one of the two proved failure conditions from Lemma 3.1.
The authenticated remote execution therefore proves Theorem 2.1.

## 6. Audit boundary

This audit proves the mathematical reduction, verifies all stored row
invariants and hashes, and independently tests both endpoint conventions and
both failure modes.  It did not launch a second full local census.  The JSON
is nevertheless replay-sufficient: the authenticated source word and each
stored position regenerate its critical set and finite side-base set, while
the row records the exact failed target or zero intersection.  Any future
independent checker can therefore validate all 12,873 rows without trusting
an optimization solver or enumerating replacement values.
