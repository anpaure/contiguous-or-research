# Independent audit of the closed resident rigid-GK `C10` collar

**Date:** 2026-08-13  
**Audited file:**
`MATH_THEOREM_GK_C10_CLOSED_RESIDENT_COLLAR_AND_INTERNAL_DECK_MONOTONICITY_20260813.md`  
**Audited SHA256:**
`1f6b6f27633f6c6ad2adb2ddebd413b3b3679c6f15305d30b9b0262f93bc760b`  
**Verdict:** **PASS at its prospective closed-collar scope.**  The doubled
history gives five simple resident collar cycles on equal support and the
net five-hinge rethread fuses them to one.  Every exact immediate resource
is preserved and the complete cyclic owner-interval deck is support
monotone.  The theorem correctly does not claim the rooted GK `4 -> 2`
graft, arbitrary exterior transparency, zero-gap residence, or typed-cap
transport.

## 1. Screen and resource identities

With

\[
 H=\{m,\ldots,2m-3\},\quad
 \alpha=0,\quad\beta=1,\quad z=m-1,
 \quad u=2m-2,\quad v=2m-1,\quad w=2m,
\]

the ten screens are

\[
\begin{array}{c|cc}
i&X_i&Y_i\\ \hline
0&zuv&uvw\\
1&\alpha zu&\alpha uv\\
2&\alpha\beta z&\alpha\beta u\\
3&\alpha zv&\alpha\beta v\\
4&zvw&\alpha vw.
\end{array}
\]

They are distinct and satisfy

\[
 X_{i-1}\cup Y_i=X_i\cup Y_i,qquad
 X_i\cap Y_{i+1}=X_i\cap Y_i.
\]

Thus the changed seams preserve the lower colours rolewise and permute the
upper colours.  Fresh-core prefix/suffix profiles distinguish all internal
owners and colours, while the active screen distinguishes different ports.
The requirement `d<=m-3` is exactly what supplies `d` fresh labels in
`{2,...,m-2}`; it is not silently weakened to `d<=m-2`.

## 2. Closed chronology and positive residence

Each old source cycle is

\[
 P_i=(Y_i,\mathcal C',X_i,\mathcal C)
\]

of length `L=2d+2`.  Concatenating the five tagged `P_i` paths changes only
the five declared screen seams and gives one source cycle.  It uses exactly
the same `5L=10d+10` source positions and owner windows.

Every source occurrence contributes `d+1` consecutive owner occurrences.
Overlapping contributions merge rather than shorten positive components,
so every nonconstant positive run has length at least `d+1`.  This argument
does not bound zero gaps, exactly as the theorem states.

The strict-lower occurrence map is valid because an interval reaching a
left screen across a changed seam contains the full history `H` and hence
one complete owner.  Every strict-lower crossing interval is therefore a
common-history suffix followed by a tagged right-path prefix and transports
to the old seam preceding the same path.

## 3. Complete cyclic deck inclusion

Let an old owner interval lie on port `i` and have owner width `t`.

If `t<=d+1`, its source support has length `d+t<L`.  A noncrossing interval
survives literally.  For a crossing interval, retain the prefix beginning
at `Y_i` and replace the incoming suffix from port `i` by the corresponding
suffix from port `i-1`.  The fresh/core union is unchanged.  Its only
possible active change is `X_i` to `X_(i-1)`, which is absorbed by `Y_i`
because

\[
                         X_{i-1}\cup Y_i=X_i\cup Y_i.
\]

If `t>=d+2`, `d+2` owner windows already cover all `L` source letters of
the old port, so every such interval has its port-saturated value

\[
 H\cup\{y_1,\ldots,y_d\}\cup X_i\cup Y_i.
\]

The `L` consecutive new source letters

\[
                         (X_{i-1},\mathcal C,Y_i,\mathcal C')
\]

give a width-`d+2` owner interval with exactly that value.  Hence

\[
 \operatorname {Deck}_{\rm cyc}(F_{old})
 \subseteq
 \operatorname {Deck}_{\rm cyc}(F_{new})
\]

at every width.  This is set-support inclusion, not graded-multiplicity
equality.

## 4. Replay and exact boundary

The associated audit script was run on `h100` for all `104` parameter pairs

\[
 5\le m\le17,\qquad1\le d\le m-3.
\]

It independently checks screen identities, owner/q1 simplicity and resource
equality, positive residence, topology `5 -> 1`, and the complete cyclic
deck inclusion.  The result was

```text
PASS_GK_C10_CLOSED_RESIDENT_COLLAR cases=104 m=5..17 d=1..m-3
owners=q1=simple residence>=d+1 topology=5_to_1
Deck_cyc(old)<=Deck_cyc(new)
```

No extrapolation to the literal GK residual-path involution is valid from
this alone.  There, opaque paths pair `B_i` with `A_rho(i)` for
`rho=(0)(1 4)(2)(3)`, rather than closing every `B_i` back at `A_i`.
Arbitrary exterior intervals can carry private context coordinates and have
a nonzero complete upper current.  The audited theorem correctly leaves
rooted grafting, exterior witnesses, zero gaps, final opening, and typed cap
as separate requirements.

