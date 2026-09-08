# Even top-bit splice recurrence

Date: 2026-07-31  
Status: **proved recurrence; exactness and the all-odd input remain open**

## 1. Statement

Let `X=(x_1,...,x_n)` be a universal OR word on `[k-1]`, and let
`b=2^(k-1)` be the new singleton coordinate.  Put

```text
S_b(X) = X · [b] · ((x_1|b),...,(x_(n-1)|b)).
```

Then `S_b(X)` is a universal OR word on `[k]` of length `2n`.  Consequently

\[
\boxed{\nu(k)\le 2\nu(k-1)}.                    \tag{1.1}
\]

This is an unconditional recurrence: it needs only a universal predecessor,
not a carrier, residence condition, shadow factor, or compiler.

## 2. Proof

Every nonempty mask on `[k]` has one of three forms.

1. An unmarked mask `A` is delivered by its witness interval in the first
   copy `X`.
2. The mask `{b}` is the central singleton cell.
3. Write a remaining marked mask as `A union {b}` with `A` nonempty.  Choose
   any interval `x_i,...,x_j` of `X` whose OR is `A`.  If `j<n`, its marked
   copy in the final block has OR `A union {b}`.  If `j=n`, the original
   interval followed by the adjacent singleton `[b]` has OR
   `A union {b}`.

These cases exhaust all nonempty masks, proving the theorem.  The length is
`n+1+(n-1)=2n`.  ∎

## 3. Relation to the proposed lower bound

For even `k=2m`, the two relevant middle-layer sizes satisfy

\[
\binom{2m}{m}=2\binom{2m-1}{m}.
\]

Therefore, **conditional on** `nu(k-1)=B(k-1)`, the recurrence gives

\[
\nu(k)\le B(k)+2d(k-1)-d(k).                    \tag{3.1}
\]

At `k=16`, `d(15)=d(16)=3`, so (3.1) has length

\[
2B(15)=2\cdot6438=12876=B(16)+3.
\]

This does not decide `k=16`: the authoritative bracket is already

\[
12873\le\nu(16)\le12874.
\]

The closed-form splice carries six predecessor slack cells into a problem
whose lower bound allows only three.  It supplies no mechanism compressing
those six cells to three.

## 4. Correction to the claimed constant overhead

The assertion that `2d(k-1)-d(k)<=4` for every even `k`, or that the
overhead is three for every even `k>=16`, is false.  The depth parameter is
unbounded:

\[
d(k)=\Theta(\sqrt{k}).
\]

Concrete counterexamples are

```text
k=24: d(23)=4, d(24)=3, recurrence overhead 5;
k=42: d(41)=5, d(42)=4, recurrence overhead 6;
k=64: d(63)=6, d(64)=5, recurrence overhead 7.
```

More generally `2d(k-1)-d(k)=Theta(sqrt(k))`.  Thus the proved consequence
of exact odd predecessors is an explicit `B(k)+O(sqrt(k))` even construction,
not `B(k)+O(1)`.

## 5. Exact scope

The theorem proves the recurrence (1.1).  It does **not** prove:

- `nu(k)=B(k)` for any new `k`;
- existence of optimal odd predecessors for all odd `k`;
- a constant-additive all-even bound; or
- that the displayed splice is optimal within any broader braid family.

In particular, a finite/decidable odd carrier search is not an odd existence
theorem.  The general odd multi-component/socket/compiler quantifiers remain
open.
